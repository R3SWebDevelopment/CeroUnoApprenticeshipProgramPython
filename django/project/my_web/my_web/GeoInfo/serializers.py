from rest_framework import serializers

from .models import (
    Pais,
    Estado,
    Ciudad,
)


class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = [
            'id',
            'nombre',
        ]


class EstadoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()

    class Meta:
        model = Estado
        fields = [
            'id',
            'pais',
            'nombre',
        ]


class CiudadSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Ciudad
        fields = [
            'id',
            'estado',
            'nombre',
        ]
