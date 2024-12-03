from rest_framework import serializers
from .models import Filmes
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

    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filmes
        fields = '__all__'

    def get_mssage(self, instance):
        message = ''
        return message

    #def validate_ano_lancamento(self, value):
    #    if value <= 2000:
    #        raise serializers.ValidationError("Não pode cadastrado menor de 2000.")
    #    return value

    def validate(self, instance):
        movie_year = instance['ano_lancamento']
        actors = instance['atores']
        for actor in actors:
            actor_year = actor.data_nascimento.year
            if actor_year >= movie_year:
                raise serializers.ValidationError(f"Não é possível ator {actor.nome} com a data de nascimento ({actor_year}) no ano de lançamento do filme({movie_year}).")
        return instance
