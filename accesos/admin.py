from django.contrib import admin
from accesos.models import Acceso
from accesos.models import TipoAcceso

admin.site.register(Acceso)
admin.site.register(TipoAcceso)