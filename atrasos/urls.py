from django.urls import path
from atrasos.views import navegacion_dashboard_atrasos, agregar_add_atrasos, look_buscar_vuelo_atrasos

urlpatterns = [
    path('', navegacion_dashboard_atrasos, name = 'dashboard_atrasos'),
    path('agregar_atraso/', agregar_add_atrasos, name = 'add_atrasos' ),
    path('buscar_vuelo_agregar_atras/', look_buscar_vuelo_atrasos, name = 'buscar_vuelo_atrasos')
]