from rest_framework import serializers
from .models import Ator

class AtorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ator
        fields = '__all__'

    # def validate(self, data):
    #     if data['ano_lancamento'] < data['data_nascimento']:
    #         raise serializers.ValidationError('O ano de lançamento não pode ser anterior ao ano de nascimento do ator.')
    #     return data