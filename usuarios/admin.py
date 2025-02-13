from django.contrib import admin
from usuarios.models import Usuario, Role, CategoriaRole

admin.site.register(Usuario)
admin.site.register(Role)
admin.site.register(CategoriaRole)
