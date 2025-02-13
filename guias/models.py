from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Guia(models.Model):
    id_guia = models.AutoField(primary_key = True )    
    TIPOS_GUIA ={
        "Alineamiento":"Alineamiento",
        "Comunicación":"Comunicación",
        "Amabilidad":"Amabilidad",
        "Liderazgo":"Liderazgo",
        "Negociación":"Negociación",        
    }
    tipo_guia = models.CharField(
        max_length = 14 ,
        choices = TIPOS_GUIA 
    )
    explicacion = models.CharField(max_length = 250)
    
    def __str__(self):
        return f"{self.tipo_guia} - Explicacion: {self.explicacion}"
    

class Calificacion_Guia(models.Model):
    id_calificacion_guia = models.AutoField(primary_key = True )
    usuario_calificador = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    guia = models.ForeignKey(Guia, on_delete = models.CASCADE)
    calificacion = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    observacion = models.CharField(max_length = 100)
    fecha_calificacion = models.DateField(auto_now = False, auto_now_add = False)
    
    def __str__(self):
        return f"Guía {self.id_calificacion_guia} - {self.usuario_calificador.nombre} - {self.calificacion} - {self.fecha_calificacion} "