from django.urls import path
from atrasos.views import navegacion_dashboard_atrasos, agregar_add_atrasos

urlpatterns = [
    path('', navegacion_dashboard_atrasos, name = 'dashboard_atrasos'),
    path('agregar/', agregar_add_atrasos, name = 'add_atrasos' )
]