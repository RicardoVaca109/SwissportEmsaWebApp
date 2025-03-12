from django.db import models
from vuelos.models import Vuelo
# Create your models here.
class Atraso(models.Model): # Table Atrasos/ Tabla Atrasos
    id_atraso = models.AutoField(primary_key = True)
    vuelo = models.ForeignKey(Vuelo, on_delete = models.CASCADE)
    fecha_atraso = models.DateField(auto_now = False, auto_now_add = False)
    codigo_atraso = models.CharField(max_length = 10)
    minutos = models.IntegerField(default = 0)
    motivo_atraso = models.CharField(max_length = 250)
    
    def  __str__(self):
        return f"Vuelo: {self.vuelo.codigo_del_vuelo} | Matrícula: {self.vuelo.aeronave.matricula_aeronave} | Destino: {self.vuelo.destino_vuelo} |Fecha: {self.fecha_atraso} | Codigo: {self.codigo_atraso} | Motivo: {self.motivo_atraso}"