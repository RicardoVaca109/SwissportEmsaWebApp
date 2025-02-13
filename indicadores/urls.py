from django.urls import path
from indicadores.views import navegacion_dashboard_indicadores

urlpatterns = [
    path('', navegacion_dashboard_indicadores, name = 'dashboard_indicadores')
]