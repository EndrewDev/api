from django.db import models
from generos.models import Generos
from atores.models import Ator

# Create your models here.

class Filmes(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT, related_name='filmes')
    ano_lancamento = models.IntegerField(blank=True, null=True)
    atores = models.ManyToManyField(Ator, blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo