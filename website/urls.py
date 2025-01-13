# Import necessary Libraries
# Importar librerias necesarias
from django.urls import path
from . import views

urlpatterns = [
   path('', views.navegacion_dashboard_general, name = "dashboard_general")
]