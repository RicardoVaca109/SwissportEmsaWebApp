# Import necessary Libraries
# Importar librerias necesarias
from django.urls import path, include

urlpatterns = [
    path('dashboard/', include('website.urls.dashboard_urls')),
]