from django.urls import path
from guias.views import navegacion_dashboard_guias

urlpatterns = [
    path('', navegacion_dashboard_guias, name = 'dashboard_guias' )
]
