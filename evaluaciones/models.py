from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Evaluacion(models.Model):
    
    TIPOS_EVALUACION ={
        "Teórica":"Teorica",
        "Práctica":"Práctica",
    }
    
    id_evaluacion = models.AutoField(primary_key = True )
    usuario_que_califica = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario_calificado = models.ForeignKey(Usuario, related_name="usuario_calificado", on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(
        max_length = 10, 
        choices = TIPOS_EVALUACION
    ) 
    calificacion = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    observacion = models.CharField(max_length = 100)
    fecha_calificacion = models.DateField(auto_now = False, auto_now_add = False)
    def __str__(self):
        return f"Evaluación {self.id_evaluacion} - {self.usuario_calificado.nombre} - {self.tipo_evaluacion} - {self.fecha_calificacion}"
