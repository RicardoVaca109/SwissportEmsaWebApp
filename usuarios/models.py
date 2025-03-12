from django.db import models
from aeropuertos.models import Aeropuerto

# Create your models here.

class CategoriaRole(models.Model):
    id_categoria_rol = models.AutoField(primary_key = True)
    NOMBRE_ROL_CATEGORIA_CHOICES = {
        "Focal":"Focal",
        "PAX":"PAX",
        "Ventas": "Ventas",
        "Agente":"Agente",
        "High-Value":"High-Value",
        "Equipajes":"Equipajes",  
        "Control":"Control",
        "Sin Rol":"Sin Rol",  
    }
    nombre_categoria = models.CharField(max_length=15, unique=True, choices = NOMBRE_ROL_CATEGORIA_CHOICES)

    def __str__(self):
        return self.nombre_categoria


class Role(models.Model): # Table Roles / Tabla Roles
    id_rol = models.AutoField(primary_key = True) # Primary id /Id Primario
    
    # Dictionary for ENUM /  Diccionario python para datos ENUM
    NOMBRE_ROL_CHOICES = {
        "Administrador":"Administrador",
        "KAM Nacional": "KAM Nacional",
        "KAM":"KAM",
        "Supervisor":"Supervisor",
        "Station Manager":"Station Manager",
        "Lead":"Lead",
        "Agente":"Agente",
        "Gerente de Operaciones":"Gerente de Operaciones",
        "OJT":"OJT",
        "Sin Categoria Rol":"Sin Categoria Rol",    
    }
    
    nombre_rol = models.CharField(
        max_length = 50,
        unique = True,
        choices = NOMBRE_ROL_CHOICES
    )
    
    def __str__(self):
            return f"{self.nombre_rol}"



class Usuario(models.Model): # Table Usuarios / Tabla Usuario
    id_usuario = models.AutoField(primary_key=True)
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)
    categoria_rol = models.ForeignKey(CategoriaRole,on_delete=models.CASCADE, blank=True, null=True )
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique=True)
    contrasenia = models.CharField(max_length=300, unique=True)
    fecha_ingreso = models.DateField(auto_now = False, auto_now_add = False)
    bp = models.CharField(max_length=8, unique=True, blank=True, null=True)  # Identificación única de 8 números (opcional)
    erp = models.CharField(max_length=8, unique=True, blank=True, null=True) # Identificación única de 8 números (opcional)
    estatus = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo')
    ubicacion = models.CharField(max_length = 10, choices = [('Bajo Ala', 'Bajo Ala'), ('Sobre Ala', 'Sobre Ala')]) 
    
    UBICACION_USUARIO = {
        "Bajo Ala":"Bajo Ala",
        "Sobre Ala": "Sobre Ala"
    }
    
    ubicacion = models.CharField(
        max_length = 10,
        choices = UBICACION_USUARIO       
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.rol} - {self.categoria_rol} - {self.apellido} - {self.email}"