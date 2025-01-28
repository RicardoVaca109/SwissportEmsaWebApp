# Import neccesary libraries / Importar librerias necesarias
from django.contrib import admin

# Import the models / Importar los modelos
from website.models import Role
from website.models import Aeropuerto
from website.models import Usuario
from website.models import Vuelo
from website.models import Evento
from website.models import Atraso
from website.models import Acceso
from website.models import Prueba
from website.models import Resultado

# Register your models here.
# Registrar los modelos aquí
admin.site.register(Role) # Table roles / tabla roles
admin.site.register(Aeropuerto) # Table aeropuertos / tabla aeropuertos
admin.site.register(Usuario)# Table Usuarios / tabla usuarios
admin.site.register(Vuelo)# Table Vuelos / tabla vuelos
admin.site.register(Evento) # Table Eventos / tabla eventos
admin.site.register(Atraso) # Table Atrasos / tabla atrasos
admin.site.register(Acceso) # Table Acceso / tabla acceso
admin.site.register(Prueba) # Table Prueba/ tabla prueba
admin.site.register(Resultado) # Table Resultados / tabla resultado