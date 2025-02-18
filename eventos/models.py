from django.db import models
from vuelos.models import Vuelo 
from usuarios.models import Usuario
# Create your models here.
class Evento(models.Model): # Table Eventos/ Tabla Eventos
    id_evento = models.AutoField(primary_key = True)
    vuelo = models.ForeignKey(Vuelo, on_delete = models.CASCADE) # Obtener el dato de Origen del vuelo
    fecha_evento = models.DateField(auto_now = False, auto_now_add = False)
    evento_lir = models.CharField(max_length = 3)
    evento_pax = models.CharField(max_length = 3)
    motivo = models.CharField(max_length = 250)
    
    # Dictionary for ENUM /  Diccionario python para datos ENUM
    TIPO_EVENTO_CHOICES = {
        "SPI":"SPI",
        "NO SPI":"NO SPI"
    }
    
    tipo_evento = models.CharField(
        max_length = 10,
        choices = TIPO_EVENTO_CHOICES
    )
    
    plan_de_accion = models.CharField(max_length = 250)
    usuario_involucrado = models.ForeignKey(Usuario, on_delete = models.CASCADE) 
    
    def __str__(self):
        return f"Vuelo: {self.vuelo.codigo_del_vuelo} - {self.vuelo.origen_vuelo} - {self.tipo_evento} - {self.evento_lir} - {self.evento_pax}"