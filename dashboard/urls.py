from django.urls import path, include
from dashboard.views import navegacion_dashboard_general, navegacion_dashboard_rol_ojt, navegacion_dashboard_rol_kam_supervisor

urlpatterns = [
    # path('', include('website.urls.auth_urls')),
    # path('dashboard/', navegacion_dashboard_general, name='dashboard_general'),
    path('dashboard_ojt/', navegacion_dashboard_rol_ojt, name = 'dashboard_rol_ojt' ),
    path('dashboard_kams_super/', navegacion_dashboard_rol_kam_supervisor, name = 'dashboard_rol_kam_supervisor' ),
    path('', navegacion_dashboard_general, name='dashboard_general'),
    path('aeropuertos/', include('aeropuertos.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('vuelos/', include('vuelos.urls')),
    path('atrasos/', include('atrasos.urls')),
    path('eventos/', include('eventos.urls')),
    path('accesos/', include('accesos.urls'))
]
