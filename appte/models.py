from django.db import models
from django.contrib.auth.models import User


"""
class Item(models.Model):
    nome=models.CharField(max_length=80)

    def __str__(self):
        return self.nome
"""

class Produto(models.Model):
    nome=models.CharField(max_length=80)

    def __str__(self):
        return self.nome

class CarrinhoItem(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} - {self.produto.nome}"
