from rest_framework import serializers
from api.models import Equipo, Jugador

class EquipoSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un equipo.
    """
    goals_count = serializers.ReadOnlyField()
    class Meta:
        model = Equipo
        fields = ['id','goals_count','name','city']


class JugadorSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un jugador.
    """
    equipo = serializers.CharField(source='equipo.name')
    class Meta:
        model = Jugador
        fields = ['id','name','goals','equipo']        