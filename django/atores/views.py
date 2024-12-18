from rest_framework import generics
from .models import Ator
from .serializers import AtorModelSerializer, AtoresSerializer
# Create your views here.

class AtorListCreateView(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtoresSerializer

class AtorUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorModelSerializer
