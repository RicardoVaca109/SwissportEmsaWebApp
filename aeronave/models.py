from django.db import models

class Aeronave(models.Model):
    id_aeronave = models.AutoField(primary_key = True)
    TIPO_AERONAVE = {
        "Cargo":"Cargo",
        "PAX":"PAX"
    }
    tipo_de_aeronave =  models.CharField (max_length = 6, choices =TIPO_AERONAVE )
    matricula_aeronave = models.CharField(max_length = 10)
    nombre_aeronave = models.CharField(max_length = 30)
    aerolinea = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"Aeronave: {self.tipo_de_aeronave} - Matricula: {self.matricula_aeronave} - Nombre: {self.nombre_aeronave} - Aerolinea: {self.aerolinea} "
