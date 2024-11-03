from django.db import models
from generos.models import Genero
from atores.models import Ator
# Create your models here.

class Filme_titulo(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filmes')
    ano_de_lancamento = models.IntegerField(null=True, blank=True)
    atores = models.ManyToManyField(Ator, related_name='filmes')
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo