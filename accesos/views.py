from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db import transaction
from accesos.models import Acceso
from accesos.models import TipoAcceso
from usuarios.models import Usuario

def look_buscar_usuario_accesos(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para Buscar accesos")
        return redirect('login_view')
    query_busqueda_usuario = request.GET.get('q', '').strip()
    query_bp = request.GET.get('bp', '').strip()
    query_epr = request.GET.get('epr', '').strip()
    
    usuarios_activos = None  
    accesos_usuarios = {}  
    
    if query_busqueda_usuario or (query_bp and query_bp.isdigit()) or (query_epr and query_epr.isdigit()):
        usuarios_activos = Usuario.objects.filter(estatus='Activo')
        

        if query_busqueda_usuario:
            usuarios_activos = usuarios_activos.filter(
                Q(nombre__icontains=query_busqueda_usuario) |
                Q(apellido__icontains=query_busqueda_usuario)
            )
        
        if query_bp and query_bp.isdigit():
            usuarios_activos = usuarios_activos.filter(bp__icontains=query_bp)
        
        if query_epr and query_epr.isdigit():
            usuarios_activos = usuarios_activos.filter(epr__icontains=query_epr)
        
        # Obtener accesos para cada usuario y almacenarlos en el diccionario
        for usuario in usuarios_activos:
            accesos_usuarios[usuario.id_usuario] = list(Acceso.objects.filter(usuario=usuario))

    return render(request, 'buscar_usuario_accesos.html', {
        "usuarios_activos": usuarios_activos,
        "accesos_usuarios": accesos_usuarios,
        "query_busqueda_usuario": query_busqueda_usuario,
        "query_bp": query_bp,
        "query_epr": query_epr
    })

def agregar_add_accesos(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para Buscar accesos")
        return redirect('login_view')
    query_busqueda_usuario = request.GET.get('q', '').strip()
    query_bp = request.GET.get('bp', '').strip()
    query_epr = request.GET.get('epr', '').strip()

    usuarios_activos = Usuario.objects.filter(estatus='Activo')
    tipos_acceso = TipoAcceso.objects.all() # Obtener los accesos todos

    if query_busqueda_usuario:
            usuarios_activos = usuarios_activos.filter(
                nombre__icontains=query_busqueda_usuario
            ) | usuarios_activos.filter(
                apellido__icontains=query_busqueda_usuario
            )
    if query_bp and query_bp.isdigit():
        usuarios_activos = usuarios_activos.filter(bp__icontains=query_bp)
    if query_epr and query_epr.isdigit():
        usuarios_activos = usuarios_activos.filter(epr__icontains=query_epr)

    if request.method == "POST":
        id_usuario = request.POST.get("id_usuario")
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        
        # Obtener accesos existentes del usuario
        accesos_existentes = Acceso.objects.filter(usuario=usuario).values_list("tipo_acceso_id", flat=True)

        # Guardar accesos seleccionados en una transacción
        with transaction.atomic():
            for acceso in tipos_acceso:
                estado_acceso = request.POST.get(f"acceso_{acceso.id_tipo_acceso}")

                if estado_acceso and acceso.id_tipo_acceso not in accesos_existentes:
                    nuevo_acceso = Acceso(
                        usuario=usuario,
                        tipo_acceso=acceso,
                        tiene_acceso=estado_acceso
                    )
                    nuevo_acceso.save()

        return redirect('add_accesos_usuarios')

    return render(request, 'add_accesos_tmp.html', {
        "usuarios_activos": usuarios_activos,
        "tipos_acceso": tipos_acceso,
        "query_busqueda_usuario": query_busqueda_usuario,
        "query_bp": query_bp,
        "query_epr": query_epr,
    })