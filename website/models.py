from django.db import models

# Create your models here.
# Crear los modelos de la base de Datos

# Models / Modelos
class Role(models.Model): # Table Roles / Tabla Roles
    id_rol = models.AutoField(primary_key = True) # Primary id /Id Primario
    
    # Dictionary for ENUM /  Diccionario python para datos ENUM
    NOMBRE_ROL_CHOICES = {
        "Administrador":"Administrador",
        "KAM Nacional": "KAM Nacional",
        "KAM":"KAM",
        "Supervisor":"Supervisor",
        "OJT":"OJT",
        "Empleado":"Empleado"        
    }
    
    nombre_rol = models.CharField(
        max_length = 50,
        choices = NOMBRE_ROL_CHOICES
    )
    
    def __str__(self):
        return self.nombre_rol
    

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
        choices = TIPO_AEROPUERTO_CHOICES,
        null = True,
        blank = True
    )
    
    def __str__(self):
        return  f"{self.estacion_aeropuerto} - {self.nombre} ({self.ciudad}, {self.pais} - Tipo {self.tipo_aeropuerto})"
    
    
class Usuario(models.Model): # Table Usuarios / Tabla Usuario
    id_usuario = models.AutoField(primary_key = True)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE)
    id_rol = models.ForeignKey(Role, on_delete = models.CASCADE )
    nombre = models.CharField(max_length = 80)
    apellido = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 100, unique = True)
    contrasenia = models.CharField(max_length = 300, unique = True)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"
    
    
class Vuelo(models.Model): # Table Vuelos/ Tabla Vuelos
    id_vuelo = models.AutoField(primary_key = True)
    fecha_vuelo = models.DateField(auto_now = False, auto_now_add = False)
    codigo_del_vuelo = models.CharField(max_length = 15)
    origen_vuelo = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE, related_name = 'vuelos_origen')
    destino_vuelo = models.ForeignKey(Aeropuerto, on_delete = models.CASCADE, related_name = 'vuelos_destino')
    
    def __str__(self):
        return f"Vuelo: {self.codigo_del_vuelo}: {self.origen_vuelo} -> {self.destino_vuelo} | Fecha: ({self.fecha_vuelo})"
    
    
class Evento(models.Model): # Table Eventos/ Tabla Eventos
    id_evento = models.AutoField(primary_key = True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete = models.CASCADE)
    
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
        return f"Vuelo: {self.id_vuelo.codigo_del_vuelo} - {self.tipo_evento} - {self.evento_lir} - {self.evento_pax}"
    
    
class Atraso(models.Model): # Table Atrasos/ Tabla Atrasos
    id_atraso = models.AutoField(primary_key = True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete = models.CASCADE)
    fecha_atraso = models.DateField(auto_now = False, auto_now_add = False)
    codigo_atraso = models.CharField(max_length = 5)
    motivo_atraso = models.CharField(max_length = 100)
    
    def  _str_(self):
        return f"Vuelo: {self.id_vuelo.codigo_del_vuelo} | Fecha: {self.fecha_atraso} | Codigo: {self.codigo_atraso} | Motivo: {self.motivo_atraso}"