from django.db import models


class ComunidadeEscolar(models.Model):
    matricula = models.IntegerField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    vinculo = models.CharField(max_length=50)
    turmaouDisciplina = models.CharField(max_length=50)

class Usuarios(models.Model):
    credencial = models.IntegerField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=6)

class Emprestimo(models.Model):
    idEmprestimo = models.AutoField(primary_key=True)
    dataSaida = models.DateField()
    dataDevolucao = models.DateField()
    comunidadeEscolar = models.ManyToManyField(ComunidadeEscolar)
    usuarios = models.ManyToManyField(Usuarios)

class TipoProduto(models.Model):
    idTipoProduto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Produtos(models.Model):
    idProduto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idTipoProduto = models.ForeignKey(TipoProduto, on_delete=models.PROTECT)
    idEmprestimo = models.ForeignKey(Emprestimo, on_delete=models.PROTECT)

class Entrega(models.Model):
    idEntrega = models.AutoField(primary_key=True)
    dataSaida = models.DateField()
    quantidade = models.IntegerField()
    usuario = models.ManyToManyField(Usuarios)
    produto = models.ManyToManyField(Produtos)