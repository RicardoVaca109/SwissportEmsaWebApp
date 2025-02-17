from django.urls import path
from eventos.views import navegacion_dashboard_eventos, agregar_add_eventos

urlpatterns = [
    path('', navegacion_dashboard_eventos, name = 'dashboard_eventos'),
    path('agregar_eventos/', agregar_add_eventos, name = 'add_eventos' )
]