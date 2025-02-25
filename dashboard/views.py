from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# Crear las rutas para las vistas en ese archivo

def navegacion_dashboard_general(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Usuario')
    return render(request, "dashboard_general.html", {"usuario_nombre":usuario_nombre})

def navegacion_dashboard_rol_ojt(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Usuario')
    return render(request, "dashboard_rol_ojt.html", {"usuario_nombre": usuario_nombre})

def navegacion_dashboard_accesos(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Usuario')
    return render(request, "dashboard_accesos.html", {"usuario_nombre": usuario_nombre})