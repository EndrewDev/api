from django.shortcuts import get_object_or_404
from .models import Filmes
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import generics
# from .serializers import FilmesSerializer

# Create your views here.

@csrf_exempt
def filmes_view(request):
    if request.method == "GET":
        filmes = Filmes.objects.all()
        data = [{'id': filme.id, 'nome': filme.nome_filme, 'tipo': filme.tipo} for filme in filmes]
        return JsonResponse(data, safe=False, status=200)
    elif request.method == 'POST':
        dados = json.load(request.body.decode('utf-8'))
        novo_filme = Filmes(nome_file=dados['nome_filme'])
        novo_filme.save()
        return JsonResponse({'id': novo_filme.id, 'nome': novo_filme.nome_filme, 'tipo': novo_filme.tipo}, status=200)

@csrf_exempt
def view_detalhes_ataulizar_deleta(request, pk):
    detalhes = get_object_or_404(Filmes, pk=pk)

    if request.method == 'GET':
        dados = [{'id': detalhe.id, 'nome': detalhe.nome_filme, 'tipo': detalhe.tipo} for detalhe in detalhes]
        return JsonResponse(dados, status=200)
    elif request.method == 'POST':
        dados = json.load(request.body.decode('utf-8'))['nome_filme']
        detalhes.nome_filme = dados
        detalhes.save()
        return JsonResponse({'ID': detalhes.id, 'Nome filme': detalhes.nome_filme, 'Tipo': detalhes.tipo}, status=201)
    elif request.method == 'DELETE':
        detalhes.delete()
        return JsonResponse({'msg': 'Objeto já deletado com sucesso'}, status=204)

# class FilmeCreateListView(generics.ListCraeteAPIView):
#     queryset = Filmes.objects.all()
#     serializer_class = FilmesSerializer