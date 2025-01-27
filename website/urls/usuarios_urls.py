from django.urls import path
from website.views.usuarios_view import navegacion_dashboard_usuarios, agregar_add_usuarios

urlpatterns = [
    
    path('', navegacion_dashboard_usuarios, name ='dashboard_usuarios' ),
    path('agregar/', agregar_add_usuarios, name = 'add_usuarios')
]