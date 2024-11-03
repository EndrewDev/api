from django.shortcuts import render
from rest_framework import generics
from .models import Ator
from .serializers import AtorSerializer

# Create your views here.

class AtorListCreate(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer

class AtorRestrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer