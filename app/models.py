from django.db import models

class Veiculo(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    valor = models.FloatField()
    cilindradas = models.IntegerField()
    cavalos = models.IntegerField()
    

class Cliente(models.Model):
    Nome = models.CharField(max_length=150)
    Pai = models.CharField(max_length=100)
    Mae = models.CharField(max_length=100)
    CPF = models.IntegerField()
    RG = models.IntegerField()
    Nasc = models.IntegerField()
    Endereco = models.CharField(max_length=150)

