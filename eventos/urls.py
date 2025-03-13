from django.urls import path
from eventos.views import navegacion_dashboard_eventos, agregar_add_eventos,look_buscar_usuario_eventos, look_buscar_vuelo_eventos, editar_edit_evento, eliminar_delete_evento

urlpatterns = [
    path('', navegacion_dashboard_eventos, name = 'dashboard_eventos'),
    path('agregar_eventos/', agregar_add_eventos, name = 'add_eventos' ),
    path('buscar_usuario_asignar_eventos/', look_buscar_usuario_eventos, name = 'buscar_usuario_eventos'),
    path('buscar_vuelo_asignar_eventos/', look_buscar_vuelo_eventos, name = 'buscar_vuelo_eventos'),
    path('editar/<int:id_evento>/', editar_edit_evento, name = 'edit_evento'),
    path('eliminar/<int:id_evento>/', eliminar_delete_evento, name = 'delete_evento')
]