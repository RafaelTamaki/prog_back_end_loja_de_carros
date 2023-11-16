from re import A
from django.db import models

class Nome(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Montadora(models.Model):
    montadora = models.CharField(max_length=100)

    def __str__(self):
        return self.montadora

class Itens(models.Model):
    itens = models.CharField(max_length=100)

    def __str__(self):
        return self.itens

class Carro (models.Model):
    nome = models.ManyToManyField (Nome)
    ano_fabricado = models.CharField(max_length=4)
    itens = models.ManyToManyField (Itens)
    montadora = models.ManyToManyField (Montadora)

    def __str__(self):
        nomes = ", ".join([nome.nome for nome in self.nome.all()])
        return f"Carro {nomes} fabricado em {self.ano_fabricado}"
    
