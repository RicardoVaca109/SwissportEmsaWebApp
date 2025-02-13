from django.urls import path
from eventos.views import navegacion_dashboard_eventos

urlpatterns = [
    path('', navegacion_dashboard_eventos, name = 'dashboard_eventos')
]