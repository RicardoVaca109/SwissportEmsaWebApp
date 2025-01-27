from django.urls import path
from website.views.vuelos_view import navegacion_dashboard_vuelos, agregar_add_vuelos

urlpatterns = [
    # Principal Route/ Ruta principal
    path('', navegacion_dashboard_vuelos, name = 'dashboard_vuelos'),
    path('agregar/', agregar_add_vuelos, name = 'add_vuelos')
]