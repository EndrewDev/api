from rest_framework import serializers
from .models import Avalicao

class AvalicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avalicao
        fields = "__all__"
