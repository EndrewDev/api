from rest_framework import serializers
from .models import Filmes
from generos.models import Generos
from atores.models import Ator
from django.db.models import Avg

#Serializer:
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

#Serializer com Model:
class FilmeModelSerializer(serializers.ModelSerializer):

    media_avaliacao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filmes
        fields = "__all__"

    # Se o ator for maior data nascimento do que um filme lançamento, vai se um error:
    def validate(self, instance):
        print(instance)
        movie_year = instance["ano_lancamento"]
        actors = instance["atores"]

        if not movie_year:
            raise serializers.ValidationError("O ano de lançamento do filme é obrigatório.")

        for actor in actors:
            if not actor.data_nascimento:
                raise serializers.ValidationError(f"O ator {actor.nome} não possui uma data de nascimento válida.")

            actor_year = actor.data_nascimento.year

            if actor_year >= movie_year:
                raise serializers.ValidationError(
                    f"Não é possível ator {actor.nome} com a data de nascimento ({actor_year}) no ano de lançamento do filme({movie_year})."
                    )
            
        return instance
    
    # Avaliação
    def get_media_avaliacao(self, instance):
        media_avaliacoes = instance.avalicoes.aggregate(valor_medio=Avg('estrelas'))['valor_medio']

        if media_avaliacoes:
            return round(media_avaliacoes, 1)
        
        return None
    