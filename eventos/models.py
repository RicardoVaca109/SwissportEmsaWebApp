from django.db import models
from vuelos.models import Vuelo

# Create your models here.
class Evento(models.Model): # Table Eventos/ Tabla Eventos
    id_evento = models.AutoField(primary_key = True)
    vuelo = models.ForeignKey(Vuelo, on_delete = models.CASCADE)
    
    # Dictionary for ENUM /  Diccionario python para datos ENUM
    TIPO_EVENTO_CHOICES = {
        "SPI":"SPI",
        "NO SPI":"NO SPI"
    }
    
    tipo_evento = models.CharField(
        max_length = 10,
        choices = TIPO_EVENTO_CHOICES
    )
    
    observacion = models.CharField(max_length = 250)
    evento_lir = models.CharField(max_length = 3)
    evento_pax = models.CharField(max_length = 3)
    
    def __str__(self):
        return f"Vuelo: {self.vuelo.codigo_del_vuelo} - {self.tipo_evento} - {self.evento_lir} - {self.evento_pax}"