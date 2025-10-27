from django.db import models

class ComunidadeEscolar(models.Model):
    matricula = models.IntegerField('Matrícula', primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    vinculo = models.CharField('Vínculo', max_length=50)
    turmaouDisciplina = models.CharField('Turma ou Disciplina', max_length=50)

class Usuarios(models.Model):
    credencial = models.IntegerField('Credencial', primary_key=True)
    nome = models.CharField('Usuário', max_length=100)
    senha = models.CharField('Senha', max_length=6)

class TipoProduto(models.Model):
    nome = models.CharField('Tipo do Produto', max_length=100)

class Produtos(models.Model):
    nome = models.CharField('Produto', max_length=100)
    marca = models.CharField('Marca', max_length=50)
    tipoProduto = models.ForeignKey(TipoProduto, on_delete=models.PROTECT)

class Emprestimo(models.Model):
    idEmprestimo = models.AutoField('Empréstimo', primary_key=True)
    dataSaida = models.DateField('Data de Saída')
    dataDevolucao = models.DateField('Data de Devolução')
    produtos = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    comunidadeEscolar = models.ForeignKey(ComunidadeEscolar, on_delete=models.PROTECT)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.PROTECT)