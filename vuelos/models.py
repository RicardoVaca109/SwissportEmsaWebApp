from django.db import models
from aeropuertos.models import Aeropuerto
from aeronave.models import Aeronave
# Create your models here.
class Vuelo(models.Model): # Table Vuelos/ Tabla Vuelos
    id_vuelo = models.AutoField(primary_key = True)
    fecha_vuelo = models.DateField(auto_now = False, auto_now_add = False)
    codigo_del_vuelo = models.CharField(max_length = 15)
    origen_vuelo = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE, related_name = 'vuelos_origen')
    destino_vuelo = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE, related_name = 'vuelos_destino')
    escala_intermedia = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE, blank=True, null=True )
    aeronave = models.ForeignKey(Aeronave, on_delete = models.CASCADE)
    hora_salida = models.TimeField(auto_now=False, auto_now_add=False)
    hora_llegada = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"Vuelo: {self.codigo_del_vuelo}: {self.origen_vuelo} -> {self.escala_intermedia} -> {self.destino_vuelo}  | {self.aeronave} | Fecha: ({self.fecha_vuelo})"
