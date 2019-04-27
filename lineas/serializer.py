from .models import Linea, Estaciones
from rest_framework import serializers

class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estaciones
        fields = ('nombre', 'distancia')

class LineaSerializer(serializers.HyperlinkedModelSerializer):
    estaciones = EstacionSerializer(many=True, read_only=True)

    class Meta:
        model = Linea
        fields = ('nombre', 'ubicacion', 'estaciones')