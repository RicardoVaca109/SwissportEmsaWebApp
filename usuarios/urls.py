from django.urls import path
from usuarios.views import navegacion_dashboard_usuarios, agregar_add_usuarios

urlpatterns = [
    
    path('', navegacion_dashboard_usuarios, name ='dashboard_usuarios' ),
    path('agregar_usuario/', agregar_add_usuarios, name = 'add_usuarios')
]