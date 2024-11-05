from rest_framework import serializers
from .models import Filmes
# from django.db.models import Avg
from generos.models import Generos
from atores.models import Ator

class FilmeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField()
    genero = serializers.PrimaryKeyRelatedField(queryset=Generos.objects.all(), many=False)
    ano_lancamento = serializers.IntegerField()
    atores = serializers.PrimaryKeyRelatedField(queryset=Ator.objects.all(), many=True)
    resumo = serializers.CharField()

    def create(self, validated_data):
        todos_atores = validated_data.pop('atores')
        filme = Filmes.objects.create(**validated_data)
        filme.atores.set(todos_atores)
        return filme

class FilmeModelSerializer(serializers.ModelSerializer):

    # media_avaliacao = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Filmes
        fields = '__all__'

    # def get_media_avaliacao(self, instance):
    #     media_avaliacoes = instance.aggregate(valor_medio=Avg('estrelas'))['valor_medio']

    #     if media_avaliacoes:
    #         return round(media_avaliacoes, 1)
    #     return None

    # def validated_ano_lancamento(self, value):
    #     if value < 2000:    
    #         raise serializers.ValidationError('Não pode cadastrar menor de 2000')
    #     return value
