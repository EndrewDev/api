from rest_framework import generics
from .models import Filmes
from .serializers import FilmeSerializer
# Create your views here.

class FilmeListCreateView(generics.ListCreateAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmeSerializer

class FilmeUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmeSerializer