# Import the models necessary for the action of the main model of this app
# Importar los modelos necesarios para el funcionamiento del modelo principal de esta app
from django.db import models

# Create your models here.
class Aeropuerto(models.Model): # Table Aeropuertos / Tabla Aeropuertos
    id_aeropuerto = models.AutoField(primary_key = True)
    estacion_aeropuerto = models.CharField(max_length = 3, unique = True)
    nombre = models.CharField(max_length = 80, unique = True)
    ciudad = models.CharField(max_length = 80)
    pais = models.CharField(max_length = 80)  
    
    TIPO_AEROPUERTO_CHOICES = {
        "Internacional":"Internacional",
        "Nacional":"Nacional",
    }
    
    tipo_aeropuerto = models.CharField(
        max_length = 20,
        choices = TIPO_AEROPUERTO_CHOICES
    )
    
    def __str__(self):
        return  f"{self.estacion_aeropuerto} - {self.nombre} ({self.ciudad}, {self.pais} - Tipo {self.tipo_aeropuerto})"