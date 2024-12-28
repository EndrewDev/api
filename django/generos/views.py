# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
from .models import Generos
from rest_framework import generics
from .serializers import GenerosModelSerializer, GeneroSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class GenerosListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Generos.objects.all()
    serializer_class = GeneroSerializer

class GenerosUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Generos.objects.all()
    serializer_class = GenerosModelSerializer

# @csrf_exempt
# def generos_view(request):
#     if request.method == "GET":
#         generos = Generos.objects.all()
#         generos_dict = [{"id": genero.id, "nome": genero.nome} for genero in generos]
#         return JsonResponse(generos_dict, safe=False)
#     elif request.method == "POST":
#         dados = json.loads(request.body.decode("utf-8"))
#         novo_genero = Generos(nome=dados["nome"])
#         novo_genero.save()
#         return JsonResponse(
#             {"id": novo_genero.id, "nome": novo_genero.nome}, status=201
#         )


# @csrf_exempt
# def view_detalhar__atualizar_genero(request, pk):
#     genero = get_object_or_404(Generos, pk=pk)

#     if request.method == "GET":
#         dados = {"id": genero.id, "nome": genero.nome}
#         return JsonResponse(dados)

#     elif request.method == "PUT":
#         dados = json.loads(request.body.decode("utf-8"))["nome"]
#         genero.nome = dados
#         genero.save()
#         return JsonResponse({"id": genero.id, "nome": genero.nome})

#     elif request.method == "DELETE":
#         genero.delete()
#         return JsonResponse({"message": "Objeto deletado com sucesso"})