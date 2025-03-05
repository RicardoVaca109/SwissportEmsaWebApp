from django.urls import path
from indicadores.views import navegacion_dashboard_indicadores, look_buscar_usuario_indicadores, agregar_add_indicador

urlpatterns = [
    path('', navegacion_dashboard_indicadores, name = 'dashboard_indicadores'),
    path('buscar_usuario_agregar_indicadores/', look_buscar_usuario_indicadores, name = 'buscar_usuario_indicadores'),
    path('agregar_indicador_usuario/<int:usuario_id>/', agregar_add_indicador, name = 'add_indicador')
]