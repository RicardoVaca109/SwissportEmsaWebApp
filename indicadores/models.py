from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Indicador(models.Model):
    
    TIPOS_INDICADORES = {
        "Felicitación": "Felicitacion",
        "Amonestación": "Amonestacion",
        "Sanción": "Sancion",
        "Reposo Médico": "Reposo Medico",
    }

    id_indicador = models.AutoField(primary_key=True)
    usuario_que_registra = models.ForeignKey(Usuario, related_name="usuario_que_registra", on_delete=models.CASCADE)
    usuario_al_cual_registra = models.ForeignKey(Usuario, related_name="usuario_a_quien_registra", on_delete=models.CASCADE)
    tipo_indicador = models.CharField(
        max_length=20, 
        choices=TIPOS_INDICADORES
    )
    comentario = models.TextField()  
    fecha_creacion = models.DateField(auto_now = False, auto_now_add = False)  
    fecha_inicio =models.DateField(auto_now = False, auto_now_add = False) 
    fecha_fin = models.DateField(auto_now = False, auto_now_add = False)  

    def __str__(self):
        return f"Indicador {self.id_indicador} - {self.usuario_al_cual_registra.nombre} - {self.tipo_indicador} - {self.fecha_creacion}"

