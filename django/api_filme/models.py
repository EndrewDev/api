from django.db import models

# Create your models here.

class FILME(models.Model):
    nome_filme = models.CharField(max_length=100, verbose_name='Nome do filme')
    tipo_filme = models.CharField(max_length=50, verbose_name='Tipo do filme')

    def __str__(self):
        return self.nome_filme