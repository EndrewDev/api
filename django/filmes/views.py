from rest_framework import generics
from .models import Filmes
from .serializers import FilmeModelSerializer, FilmeSerializer
from rest_framework.permissions import IsAuthenticated

class FilmeListCreateView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Filmes.objects.all()
    serializer_class = FilmeModelSerializer

class FilmeUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Filmes.objects.all()
    serializer_class = FilmeModelSerializer