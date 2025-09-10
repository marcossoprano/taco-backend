from rest_framework import serializers
from .models import Alimento

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = ['id', 'nome', 'calorias', 'proteinas', 'carboidratos', 'gorduras']
