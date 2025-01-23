from django.urls import path, include
from website.views.dashboard_view import navegacion_dashboard_general

urlpatterns = [
    path('', navegacion_dashboard_general, name='dashboard_general'),
    path('aeropuertos/', include('website.urls.aeropuertos_urls')),
    path('usuarios/',include('website.urls.usuarios_urls')),
    path('vuelos/', include('website.urls.vuelos_urls'))
]
