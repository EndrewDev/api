from django.db import models

# Create your models here.
class Generos(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome