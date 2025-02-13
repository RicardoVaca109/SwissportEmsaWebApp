from django.urls import path
from accesos.views import navegacion_dashboard_accesos, agregar_add_accesos

urlpatterns = [
    path('', navegacion_dashboard_accesos, name = 'dashboard_accesos'),
    path('agregar/', agregar_add_accesos, name = 'add_accesos' )
]