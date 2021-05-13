from django.db import models
from django.utils import timezone

class Equipo(models.Model):
    """
    Representación de un Equipo de futbol.
    """
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        null=False,
    )

    city = models.CharField(
        max_length=255,
        verbose_name='City',
        null=False,
    )
        
    created_at = models.DateTimeField(
        default=timezone.now, 
        editable=False
    )

    updated_at = models.DateTimeField(
        default=timezone.now, 
        editable=False
    )
    
    @property
    def goals_count(self):
        """
        Permite calcular el número de goles anotados por todos sus jugadores.
        """
        goles = 0
        for jugador in self.jugadores.all():
            goles += jugador.goals
        return goles
    
    def __str__(self):
        """
        Retorna una representación como cadena de caracteres del Equipo.
        """
        return "Equipo: {0}-{1}".format(self.name, self.city)

class Jugador(models.Model):
    """
    Representación de un jugador de un equipo de futbol
    """    
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        null=False,
    )

    goals = models.IntegerField(
        verbose_name='Goals',
        null=False,
    )

    equipo = models.ForeignKey(
        Equipo,
        verbose_name='Equipo',
        related_name="jugadores",
        on_delete=models.CASCADE,
    )
    
    created_at = models.DateTimeField(
        default=timezone.now, 
        editable=False
    )

    updated_at = models.DateTimeField(
        default=timezone.now, 
        editable=False
    )

    def __str__(self):
        """
        Retorna una representación como cadena de caracteres del Jugador.
        """
        return self.name