from django.urls import path
from website.views.dashboard_view import navegacion_dashboard_general
from website.views.aeropuertos_view import navegacion_dashboard_aeropuertos

urlpatterns = [
    path('', navegacion_dashboard_general, name='dashboard_general'),
    path('aeropuertos/', navegacion_dashboard_aeropuertos, name='dashboard_aeropuertos'),
]
