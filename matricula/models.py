from django.db import models

class Estudante(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    nacionalidade = models.CharField(max_length=50)
    nome_mae = models.CharField(max_length=100)