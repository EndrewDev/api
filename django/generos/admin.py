from django.contrib import admin
from .models import Genero

# Register your models here.


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")