from django.db import models

class Produto(models.Model):
    CATEGORIA_CHOICE= [
        ('ativo', 'ativo'),
        ('inativo', 'inativo'),
    ]

    nome = models.CharField(max_length=100)
    kg = models.FloatField()
    sabor = models.CharField(max_length=100)
    preco = models.FloatField()
    ativo = models.CharField(max_length=15, choices=CATEGORIA_CHOICE)
    img = models.ImageField('foto', upload_to ="")


class EmailContato(models.Model):
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
