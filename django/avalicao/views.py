from django.shortcuts import render
from rest_framework import generics
from .models import Avalicao
from .serializers import AvalicaoSerializer

# Create your views here.

class AvalicaoListCriaView(generics.ListCreateAPIView):
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer

class AvaliacaoDetelheAtualizarDeletaleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer