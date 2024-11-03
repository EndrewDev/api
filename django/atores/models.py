from django.db import models

# Create your models here.

NACIONALIDADES = (
    ('BR', 'Brasil'),
    ('US', 'Estados Unidos'),
    ('FR', 'França'),
    ('DE', 'Alemanha'),
    ('ES', 'Espanha'),
    ('CA', 'Canadá'),
    ('AU', 'Austrália'),
    ('IN', 'Índia'),
    ('CN', 'China'),
    ('JP', 'Japão'),
    ('RU', 'Rússia'),
    ('GB', 'Reino Unido'),
    ('IT', 'Itália'),
    ('AR', 'Argentina'),
    ('MX', 'México'),
    ('PT', 'Portugal'),
    ('NL', 'Países Baixos'),
    ('CH', 'Suíça'),
    ('KR', 'Coreia do Sul'),
    ('SA', 'Arábia Saudita'),
    ('EG', 'Egito'),
    ('NZ', 'Nova Zelândia'),
    ('TR', 'Turquia'),
    ('AE', 'Emirados Árabes Unidos')
)

class Ator(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=20, blank=True, null=True, choices=NACIONALIDADES)