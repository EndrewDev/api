from django.shortcuts import render, get_list_or_404
from .models import Filmes
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def filmes_view(request):
    if request.method == "GET":
        filmes = Filmes.objects.all()
        data = [{'ID': filme.id, 'Nome': filme.nome_filme, 'Tipo': filme.tipo} for filme in filmes]
        return JsonResponse(data, safe=False, status=200)
    elif request.method == 'POST':
        dados = json.load(request.body.decode('utf-8'))
        novo_filme = Filmes(nome_file=dados['nome_filme'])
        novo_filme.save()
        return JsonResponse({'ID': novo_filme.id, 'Nome': novo_filme.nome_filme, 'Tipo': novo_filme.tipo}, status=201)

@csrf_exempt
def detalhe_filme(request, pk):
    detalhe = get_list_or_404(Filmes, pk=pk)
    dados = {'ID': detalhe.id, 'NOME FILNE': detalhe.nome_filme, 'TIPO': detalhe.tipo}
    return JsonResponse(dados)

def atualizar_filme(request, pk):
    filme = get_list_or_404(Filmes, pk=pk)
    dados = json.load(request.body.decode('utf-8'))['nome_filme']
    filme.nome_filme = dados
    filme.save()
    return JsonResponse({'ID': filme.id, 'Nome filme': filme.nome_filme, 'Tipo': filme.tipo})