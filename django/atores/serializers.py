from rest_framework import serializers
from .models import Ator

NACIONALIDADES = (
    ('BR', 'Brasil'),
    ('US', 'Estados Unidos'),
    ('FR', 'França'),
    ('DE', 'Alemanha'),
    ('ES', 'Espanha'),
    ('CA', 'Canadá'),
    ('AU', 'Austrália'),
    ('IN', 'Índia'),
    ('CN', 'China'),
    ('JP', 'Japão'),
    ('RU', 'Rússia'),
    ('GB', 'Reino Unido'),
    ('IT', 'Itália'),
    ('AR', 'Argentina'),
    ('MX', 'México'),
    ('PT', 'Portugal'),
    ('NL', 'Países Baixos'),
    ('CH', 'Suíça'),
    ('KR', 'Coreia do Sul'),
    ('SA', 'Arábia Saudita'),
    ('EG', 'Egito'),
    ('NZ', 'Nova Zelândia'),
    ('TR', 'Turquia'),
    ('AE', 'Emirados Árabes Unidos')
)

class AtorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()
    data_nascimento = serializers.DateField()
    nacionalidade = serializers.ChoiceField(choices=NACIONALIDADES)

    def create(self, validated_data):
        ator = Ator.objects.create(**validated_data)
        return ator

class AtorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ator
        fields = '__all__'

    def validate_data_nascimento(self, dataset):
        if dataset < 1995:
            raise serializers.ValidationError("Não pode cadastra menor de 1995")
        return dataset
