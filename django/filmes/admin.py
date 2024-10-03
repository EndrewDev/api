from django.contrib import admin
from .models import Filmes

# Register your models here.
@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']