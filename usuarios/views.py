from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse
from usuarios.models import Usuario
from aeropuertos.models import Aeropuerto
from usuarios.models import Role
from usuarios.models import CategoriaRole

def navegacion_dashboard_usuarios(request):
    total_usuarios = Usuario.objects.all() # Usuario.objects.select_related('id_aeropuerto', 'id_rol').all()
    return render(request, 'dashboard_usuarios.html', {'total_usuarios':total_usuarios})

def agregar_add_usuarios(request):
    
    #Obtain all category roles / Obtener las categorias de roles
    total_categorias_role = CategoriaRole.objects.all()    
    # Obtain all roles / Obtener todos los roles
    total_roles = Role.objects.all()
    # Obtain total airports / Obtener total aeropuertos 
    total_aeropuertos = Aeropuerto.objects.all()
    
    if request.method == 'POST':
        aeropuerto = request.POST.get('id_aeropuerto')
        rol = request.POST.get('id_rol')
        categoria_rol =  request.POST.get('id_categoria_rol') or None
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contrasenia = make_password(request.POST.get('contrasenia'))
        fecha_ingreso = request.POST.get('fecha_ingreso')
        bp = request.POST.get('bp') 
        erp = request.POST.get('erp') or None
        estatus = request.POST.get('estatus')
        
        # Validación básica de que la información este completa
        if aeropuerto and rol and nombre and apellido and email and contrasenia and fecha_ingreso and bp and estatus:
            Usuario.objects.create(
                aeropuerto = Aeropuerto.objects.get(pk = aeropuerto),
                rol = Role.objects.get(pk = rol),
                categoria_rol = CategoriaRole.objects.get(pk = categoria_rol) if categoria_rol else None,
                nombre = nombre,
                apellido = apellido,
                email = email,
                contrasenia = contrasenia,
                fecha_ingreso = fecha_ingreso,
                bp=bp,
                erp=erp,
                estatus=estatus       
            )
        return redirect(reverse('dashboard_usuarios'))
    return render(request, 'add_usuarios_tmp.html',{
        'total_roles':total_roles,
        'total_aeropuertos':total_aeropuertos,
        'total_categorias_role':total_categorias_role
        })
