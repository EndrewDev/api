from rest_framework import generics
from .models import Ator
from .serializers import AtorModelSerializer, AtoresSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AtorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Ator.objects.all()
    serializer_class = AtoresSerializer

class AtorUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Ator.objects.all()
    serializer_class = AtorModelSerializer
