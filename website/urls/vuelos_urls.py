from django.urls import path
from website.views.vuelos_view import navegacion_dashboard_vuelos

urlpatterns = [
    # Principal Route/ Ruta principal
    path('', navegacion_dashboard_vuelos, name = 'dahsboard_vuelos')
]