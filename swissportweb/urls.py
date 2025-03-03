"""
URL configuration for swissportweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import necessary Libraries
# Importar librerias necesarias
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('aeropuertos/', include('aeropuertos.urls')),
    path('vuelos/', include('vuelos.urls')),
    path('atrasos/', include('atrasos.urls')),
    path('eventos/', include('eventos.urls')),
    path('accesos/', include('accesos.urls')),
    path('auth/', include('auth_custom.urls')),
    path('', include('dashboard.urls')),
    path('evaluaciones/', include('evaluaciones.urls')),
    path('guias/', include('guias.urls')),
    path('indicadores/', include('indicadores.urls')),
]
