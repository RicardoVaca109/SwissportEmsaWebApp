# Import neccesary libraries / Importar librerias necesarias
from django.contrib import admin

# Import the models / Importar los modelos
from .models import Roles
from .models import Aeropuerto

# Register your models here.
# Registrar los modelos aquí
admin.site.register(Roles) # Table roles / tabla roles
admin.site.register(Aeropuerto) # Table aeropuertos / tabla aeropuertos
