from rest_framework import generics
from .models import Genero
from .serializers import GeneroSerializer


# Create your views here.

class GeneroCreateListView(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GeneroDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer