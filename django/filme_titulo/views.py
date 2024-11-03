from rest_framework import generics
from .models import Filme_titulo
from .serializers import FilmeTituloSeralizer

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    queryset = Filme_titulo.objects.all()
    serializer_class = FilmeTituloSeralizer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme_titulo.objects.all()
    serializer_class = FilmeTituloSeralizer