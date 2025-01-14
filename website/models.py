from django.db import models

# Create your models here.
# Crear los modelos de la base de Datos

# Models / Modelos
class Roles(models.Model): # Table Roles / Tabla Roles
    id_rol = models.AutoField(primary_key=True) # Primary id /Id Primario
    
    # Dictionary for ENUM /  Diccionario python para datos ENUM
    NOMBRE_ROL_CHOICES = {
        "Administrador":"Administrador",
        "KAM":"KAM",
        "Supervisor":"Supervisor"
    }
    
    nombre_rol = models.CharField(
        max_length = 50,
        choices = NOMBRE_ROL_CHOICES
    )
    
    def __str__(self):
        return self.nombre_rol

class Aeropuerto(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    estacion_aeropuerto = models.CharField(max_length=3, unique = True)
    nombre = models.CharField(max_length=80, unique=True)
    ciudad = models.CharField(max_length=80)
    pais = models.CharField(max_length=80)
    
    def __str__(self):
        return  f"{self.estacion_aeropuerto} - {self.nombre} ({self.ciudad}, {self.pais})"
    