from rest_framework import serializers
from .models import Generos

class GeneroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()

    def create(self, validated_data):
        genero = Generos.objects.create(**validated_data)
        return genero
        

class GenerosModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Generos
        fields = '__all__'