from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from usuarios.models import Usuario
from aeropuertos.models import Aeropuerto


def navegacion_dashboard_usuarios(request):
    total_usuarios = Usuario.objects.all().order_by('id_usuario') # Usuario.objects.select_related('id_aeropuerto', 'id_rol').all()
    return render(request, 'dashboard_usuarios.html', {'total_usuarios':total_usuarios})


def detalle_detail_usuarios(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario = id_usuario)
    return render(request,'detalle_usuarios_tmp.html', {
        'usuario':usuario
    })


def agregar_add_usuarios(request):
    # Obtain total airports / Obtener total aeropuertos 
    total_aeropuertos = Aeropuerto.objects.all()
    
    if request.method == 'POST':
        aeropuerto = request.POST.get('id_aeropuerto')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contrasenia = make_password(request.POST.get('contrasenia'))
        fecha_ingreso = request.POST.get('fecha_ingreso')
        cargo = request.POST.GET('cargo')
        bp = request.POST.get('bp') or None 
        epr = request.POST.get('epr') or None
        estatus = request.POST.get('estatus')
        ubicacion = request.POST.get('ubicacion')
        
        # Validación básica de que la información este completa
        if aeropuerto and nombre and apellido and email and contrasenia and fecha_ingreso and estatus and ubicacion:
            Usuario.objects.create(
                aeropuerto = Aeropuerto.objects.get(pk = aeropuerto),
                cargo = cargo,
                nombre = nombre,
                apellido = apellido,
                email = email,
                contrasenia = contrasenia,
                fecha_ingreso = fecha_ingreso,
                bp=bp,
                epr=epr,
                estatus=estatus,
                ubicacion = ubicacion       
            )
        return redirect(reverse('dashboard_usuarios'))
    return render(request, 'add_usuarios_tmp.html',{
        'total_aeropuertos':total_aeropuertos,
        })

def editar_edit_usuarios(request, id_usuario):
    
    usuario = get_object_or_404(Usuario, id_usuario = id_usuario)
    
    # Obtain total airports / Obtener total aeropuertos 
    total_aeropuertos = Aeropuerto.objects.all()
    
    if request.method == 'POST':
        usuario.aeropuerto = Aeropuerto.objects.get(pk = request.POST.get('id_aeropuerto'))
        usuario.nombre = request.POST.get('nombre')
        usuario.apellido = request.POST.get('apellido')
        usuario.email = request.POST.get('email')
        usuario.contrasenia = make_password(request.POST.get('contrasenia'))
        usuario.fecha_ingreso = request.POST.get('fecha_ingreso')
        usuario.cargo =  request.POST.GET('cargo')
        usuario.bp = request.POST.get('bp') or None 
        usuario.epr = request.POST.get('epr') or None
        usuario.estatus = request.POST.get('estatus')
        usuario.ubicacion = request.POST.get('ubicacion')
        
        nueva_contrasenia = request.POST.get('contrasenia')
        if nueva_contrasenia:
            usuario.contrasenia = make_password(nueva_contrasenia)

        usuario.save()
        return redirect(reverse('dashboard_usuarios'))
    
    return render(request, 'edit_usuarios_tmp.html', {
        'usuario': usuario,
        'total_aeropuertos': total_aeropuertos,
    })
   