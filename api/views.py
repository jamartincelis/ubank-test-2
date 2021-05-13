from api.models import Equipo, Jugador
from api.serializers import EquipoSerializer, JugadorSerializer
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
 
@authentication_classes([])
@permission_classes([])
class EquipoList(generics.ListCreateAPIView):
    """
    Permite listar y crear equipos
    """
    serializer_class = EquipoSerializer
        
    def get_queryset(self):
        """
        Se realizan los filtros de acuerdo a los parámetros ingresados
        """        
        queryset = Equipo.objects.all()
        # filtros
        nombre = self.request.query_params.get('nombre',None)
        ciudad = self.request.query_params.get('ciudad',None)
        if nombre:
            queryset = queryset.filter(name=nombre)
        if ciudad:
            queryset = queryset.filter(city=ciudad)
        return queryset
    
    
class EquipoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Equipo.
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class JugadorList(generics.ListCreateAPIView):
    """
    Permite listar y crear Jugadores.
    """
    serializer_class = JugadorSerializer
    
    def get_queryset(self):
        """
        Se realizan los filtros de acuerdo a los parámetros ingresados
        """
        queryset = Jugador.objects.all()
        # filtros
        nombre = self.request.query_params.get('nombre',None)
        goles = self.request.query_params.get('goles',None)
        equipo = self.request.query_params.get('equipo',None)
        if nombre:
            queryset = queryset.filter(name=nombre)
        if goles:
            queryset = queryset.filter(goals=goles)
        if equipo:
            queryset = queryset.filter(equipo__name=equipo)
        
        return queryset
    
    
class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Equipo.
    """    
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
