from rest_framework import serializers
from .models import Filme_titulo

class FilmeTituloSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model = Filme_titulo
        fields = '__all__'