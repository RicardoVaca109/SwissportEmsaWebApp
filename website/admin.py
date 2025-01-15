# Import neccesary libraries / Importar librerias necesarias
from django.contrib import admin

# Import the models / Importar los modelos
from .models import Role
from .models import Aeropuerto
from .models import Usuario
from .models import Vuelo
from .models import Evento
from .models import Atraso

# Register your models here.
# Registrar los modelos aquí
admin.site.register(Role) # Table roles / tabla roles
admin.site.register(Aeropuerto) # Table aeropuertos / tabla aeropuertos
admin.site.register(Usuario)# Table Usuarios / tabla usuarios
admin.site.register(Vuelo)# Table Vuelos / tabla vuelos
admin.site.register(Evento) # Table Eventos / tabla eventos
admin.site.register(Atraso) # Table Atrasos / tabla atrasos