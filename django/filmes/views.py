from django.shortcuts import render
from .models import Filmes
from django.http import JsonResponse

# Create your views here.
def filmes_view(request):
    filmes = Filmes.objects.all()
    data = [{'ID': filme.id, 'Nome': filme.nome_filme, 'Tipo': filme.tipo} for filme in filmes]
    return JsonResponse(data, safe=False, status=200)