# Import the models necessary for the action of the main model of this app
# Importar los modelos necesarios para el funcionamiento del modelo principal de esta app
from django.db import models
from usuarios.models import Usuario

# Create your models here.

class TipoAcceso(models.Model):
    id_tipo_acceso = models.AutoField(primary_key = True)
    
    TIPO_ACCESOS_CHOICES = {
        "SABRE":"SABRE",
        "RES":"RES",
        "ALLEGRO ESTÁNDAR":"ALLEGRO ESTÁNDAR",
        "ALLEGRO CHECK IN":"ALLEGRO CHECK IN",
        "ALLEGRO ONE":"ALLEGRO ONE",
        "SIGA":"SIGA",
        "WTD":"WTD",
        "ALLOW ME":"ALLOW ME",
        "PRS":"PRS",
        "AMADEUS":"AMADEUS",
        "ACCESO E BUSSINES  360":"ACCESO E BUSSINES  360",
        "ADM":"ADM",
        "BRS ":"BRS",
        "PIC":"PIC",
        "ACCESO PORTA DE PROVEEDORES":"ACCESO PORTA DE PROVEEDORES",
        "CORREO CON DOMINIO LATAM":"CORREO CON DOMINIO LATAM"
        
    }
    
    nombre_acceso = models.CharField(
        max_length = 50,
        unique=True,
        choices = TIPO_ACCESOS_CHOICES,  
    )
    
    def __str__(self):
        return self.nombre_acceso
    
class Acceso(models.Model):
    ESTADOS_ACCESOS_CHOICES = {
        "SI":"SI",
        "NO":"NO",
        "SOLICITADO":"SOLICITADO",
        "PENDIENTE":"PENDIENTE",
    }    
    id_acceso = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    tipo_acceso = models.ForeignKey(TipoAcceso, on_delete = models.CASCADE )
    tiene_acceso = models.CharField(
        max_length = 15,
        choices = ESTADOS_ACCESOS_CHOICES  
    )
    
    def __str__(self):
        return f"Acceso: {self.id_acceso} - Usuario: {self.usuario.nombre} - Tipo: {self.tipo_acceso} - Estado: {self.tiene_acceso}"

