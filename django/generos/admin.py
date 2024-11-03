from django.contrib import admin
from .models import Generos
# Register your models here.

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")