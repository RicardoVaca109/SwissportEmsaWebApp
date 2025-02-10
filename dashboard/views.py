from django.shortcuts import render

# Create your views here.
# Crear las rutas para las vistas en ese archivo

def navegacion_dashboard_general(request):
    return render(request, "dashboard_general.html")

def navegacion_dashboard_rol_ojt(request):
    return render(request, "dashboard_rol_ojt.html")

