from rest_framework import serializers
from .models import Generos

class GenerosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Generos
        fields = '__all__'