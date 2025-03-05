from django.urls import path
from eventos.views import navegacion_dashboard_eventos, agregar_add_eventos,look_buscar_usuario_eventos, look_buscar_vuelo_eventos

urlpatterns = [
    path('', navegacion_dashboard_eventos, name = 'dashboard_eventos'),
    path('agregar_eventos/', agregar_add_eventos, name = 'add_eventos' ),
    path('buscar_usuario_asignar_eventos/', look_buscar_usuario_eventos, name = 'buscar_usuario_eventos'),
    path('buscar_vuelo_asignar_eventos/', look_buscar_vuelo_eventos, name = 'buscar_vuelo_eventos')
]