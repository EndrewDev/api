from django.contrib import admin
from .models import Avalicao

# Register your models here.
@admin.register(Avalicao)
class AvalicaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'estrelas', 'comentario')