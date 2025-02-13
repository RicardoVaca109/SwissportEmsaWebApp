from django.urls import path
from evaluaciones.views import navegacion_dashboard_evaluaciones, look_buscar_empleado, evaluate_evaluar_empleado

urlpatterns = [
    path('', navegacion_dashboard_evaluaciones, name = 'dashboard_evaluaciones'),
    path('buscar_empleado/', look_buscar_empleado, name = 'buscar_empleado'),
    path('evaluar/<int:usuario_id>/<str:tipo_evaluacion>', evaluate_evaluar_empleado, name = 'evaluar_empleado')
]