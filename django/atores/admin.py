from django.contrib import admin
from .models import Ator
# Register your models here.

@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'nacionalidade')