from rest_framework import serializers
from .models import Filmes

class FilmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filmes
        fields = '__all__'