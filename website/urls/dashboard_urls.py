from django.urls import path
from website.views.dashboard_view import navegacion_dashboard_general
from website.views.aeropuertos_view import navegacion_dashboard_aeropuertos
from website.views.usuarios_view import navegacion_dashboard_usuarios

urlpatterns = [
    path('', navegacion_dashboard_general, name='dashboard_general'),
    path('aeropuertos/', navegacion_dashboard_aeropuertos, name = 'dashboard_aeropuertos'),
    path('usuarios/', navegacion_dashboard_usuarios, name = 'dashboard_usuarios')
]
