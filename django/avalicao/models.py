from django.db import models
from filmes.models import Filmes
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Avalicao(models.Model):
    filme = models.ForeignKey(
        Filmes, on_delete=models.PROTECT, related_name='avalicoes'
    )
    estrelas = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Não pode enviar um valor menor que 0.'),
            MaxValueValidator(5, 'Não pode enviar o valor maior que 5.')
        ]
    )
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.filme}: {self.estrelas}"
    