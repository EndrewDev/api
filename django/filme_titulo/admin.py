from django.contrib import admin
from .models import Filme_titulo
# Register your models here.

@admin.register(Filme_titulo)
class FilmeTituloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_de_lancamento', 'genero')