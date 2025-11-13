from django.db import models

class ComunidadeEscolar(models.Model):
    matricula = models.IntegerField('Matrícula', primary_key=True, unique=True)
    nome = models.CharField('Nome', max_length=100)
    vinculo = models.CharField('Vínculo', max_length=50)
    turmaouDisciplina = models.CharField('Turma ou Disciplina', max_length=50)

class Usuarios(models.Model):
    credencial = models.IntegerField('Credencial', primary_key=True)
    nome = models.CharField('Usuário', max_length=100)
    senha = models.CharField('Senha', max_length=128)  # Aumentado para comportar o hash

    def set_password(self, raw_password):
        """Hash e armazena a senha do usuário."""
        from django.contrib.auth.hashers import make_password
        # Apenas atualiza o atributo de senha com o hash.
        # Não salvamos aqui para evitar problemas ao criar uma instância nova
        # (quem chama pode optar por salvar explicitamente depois).
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica se a senha fornecida corresponde ao hash armazenado."""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.senha)

class TipoProduto(models.Model):
    codigo = models.IntegerField('Código do Tipo do Produto', primary_key=True, null=False)
    nome = models.CharField('Tipo do Produto', max_length=100)
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField('Produto', max_length=100)
    marca = models.CharField('Marca', max_length=50, null=True, blank=True)
    devo_ou_nao = models.BooleanField('Devolutivo ou não', default=False)
    tipoProduto = models.ForeignKey(TipoProduto, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.nome} ({self.tipoProduto.nome})"

class Emprestimo(models.Model):
    idEmprestimo = models.AutoField('Empréstimo', primary_key=True)
    dataSaida = models.DateField('Data de Saída', null=True)  # permitir nulo temporariamente
    dataDevolucao = models.DateField('Data de Devolução', null=True, blank=True)  # permitir nulo temporariamente
    entregue = models.BooleanField('Entregue', default=False)
    produtos = models.ForeignKey(Produtos, on_delete=models.PROTECT, null=True)  # permitir nulo temporariamente
    comunidadeEscolar = models.ForeignKey(ComunidadeEscolar, on_delete=models.PROTECT, null=True)  # permitir nulo temporariamente
    usuarios = models.ForeignKey(Usuarios, on_delete=models.PROTECT, null=True)  # permitir nulo temporariamente