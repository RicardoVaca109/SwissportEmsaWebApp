from django.urls import path, include
from dashboard.views import navegacion_dashboard_general, navegacion_dashboard_rol_ojt

urlpatterns = [
    # path('', include('website.urls.auth_urls')),
    # path('dashboard/', navegacion_dashboard_general, name='dashboard_general'),
    path('dashboard/ojt/', navegacion_dashboard_rol_ojt, name = 'dashboard_rol_ojt' ),
    path('', navegacion_dashboard_general, name='dashboard_general'),
    path('aeropuertos/', include('aeropuertos.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('vuelos/', include('vuelos.urls')),
    path('atrasos/', include('atrasos.urls')),
    path('eventos/', include('eventos.urls')),
    path('accesos/', include('accesos.urls'))
]
