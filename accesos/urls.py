from django.urls import path
from accesos.views import navegacion_dashboard_accesos, agregar_add_accesos, look_buscar_usuario_accesos

urlpatterns = [
    path('', navegacion_dashboard_accesos, name = 'dashboard_accesos'),
    path('buscar_usuario_accesos', look_buscar_usuario_accesos, name = 'buscar_usuario_accesos'),
    path('agregar_usuario_accesos/', agregar_add_accesos, name = 'add_accesos_usuarios' )
]