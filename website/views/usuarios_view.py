from django.shortcuts import render
from website.models import Usuario

def navegacion_dashboard_usuarios(request):
    total_usuarios = Usuario.objects.all
    return render(request, 'dahsboard_usuarios.html', {'total_usuarios':total_usuarios})
