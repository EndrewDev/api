from django.shortcuts import render
from rest_framework import generics
from .models import Avalicao
from .serializers import AvalicaoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AvalicaoListCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer

class AvaliacaoDetelheAtualizarDeletaleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = (IsAuthenticated)
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer