from rest_framework import serializers
from .models import Filmes
from django.db.models import Avg

class FilmeSerializer(serializers.ModelSerializer):

    # media_avaliacao = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Filmes
        fields = '__all__'

    # def get_media_avaliacao(self, instance):
    #     media_avaliacoes = instance.filmes.aggregate(valor_medio=Avg('estrelas'))['valor_medio']

    #     if media_avaliacoes:
    #         return round(media_avaliacoes, 1)
    #     return None

    # def validate_ano_de_lancamento(self, value):
    #     if value < 2000:
    #         raise serializers.ValidationError('Não pode cadastrar menor de 2000')
    #     return value