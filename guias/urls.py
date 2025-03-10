from django.urls import path
from guias.views import navegacion_dashboard_guias, agregar_add_calificacion_guia

urlpatterns = [
    path('', navegacion_dashboard_guias, name = "dashboard_guias" ),
    path('agregar_califcacion_guia/', agregar_add_calificacion_guia, name = 'add_calificacion_guia')
]
