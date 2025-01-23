from django.urls import path
from website.views.usuarios_view import navegacion_dashboard_usuarios

urlpatterns = [
    
    path('', navegacion_dashboard_usuarios, name ='dashboard_usuarios' )
]