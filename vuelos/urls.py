from django.urls import path
from vuelos.views import navegacion_dashboard_vuelos, agregar_add_vuelos, editar_edit_vuelos

urlpatterns = [
    # Principal Route/ Ruta principal
    path('', navegacion_dashboard_vuelos, name = 'dashboard_vuelos'),
    path('agregar_vuelo/', agregar_add_vuelos, name = 'add_vuelos'),
    path('vuelos/editar/<int:id_vuelo>', editar_edit_vuelos, name = 'edit_vuelos')
]