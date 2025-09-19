from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    credencial = models.IntegerField(max_length=100)
    senha = models.IntegerField(max_length=100)