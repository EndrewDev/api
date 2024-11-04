from rest_framework import serializers
from .models import Filmes
from django.db.models import Avg

class FilmeSerializer(serializers.ModelSerializer):

    media_avaliacao = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Filmes
        fields = '__all__'

    def get_media_avaliacao(self, instance):
        media_avaliacoes = instance.avaliacoes.aggregate(valor_medio=Avg('Estrela'))['valor_medio']

        if media_avaliacoes:
            return round(media_avaliacoes, 1)
        return None

    def validade_ano_lancamento(self, value):
        if value < 2000:
            raise serializers.ValidationError('Não pode cadastrar menor de 2000')
        return value