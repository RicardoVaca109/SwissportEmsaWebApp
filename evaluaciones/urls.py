from django.urls import path
from evaluaciones.views import navegacion_dashboard_evaluaciones, look_buscar_usuario_evaluaciones, evaluate_evaluar_usuario

urlpatterns = [
    path('', navegacion_dashboard_evaluaciones, name = 'dashboard_evaluaciones'),
    path('buscar_usuario_evaluaciones/', look_buscar_usuario_evaluaciones, name = 'buscar_usuario_evaluaciones'),
    path('evaluar/<int:usuario_id>/<str:tipo_evaluacion>', evaluate_evaluar_usuario, name = 'evaluar_usuario')
]