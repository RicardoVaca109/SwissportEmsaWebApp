from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from usuarios.models import Usuario
from indicadores.models import Indicador

def navegacion_dashboard_indicadores(request):
    total_indicadores = Indicador.objects.all()
    return render(request, 'dashboard_indicadores.html', {'total_indicadores':total_indicadores})

def look_buscar_usuario_indicadores(request):  # Buscar un empleado antes de agregarle un Indicador
    query_busqueda_usuario = request.GET.get('q','').strip()
    query_bp = request.GET.get('bp', '').strip()
    query_erp = request.GET.get('erp', '').strip()
    
    usuarios_activos = None   # Inicialmente, no se carga ningún empleado
    
    if query_busqueda_usuario or (query_bp and query_bp.isdigit()) or (query_erp and query_erp.isdigit()):
        usuarios_activos = Usuario.objects.filter(estatus='Activo')
    
        if query_busqueda_usuario:
            usuarios_activos = usuarios_activos.filter(
                Q(nombre__icontains=query_busqueda_usuario) |
                Q(apellido__icontains=query_busqueda_usuario)
            )
                
        if query_bp and query_bp.isdigit():
            usuarios_activos = usuarios_activos.filter(bp__icontains=query_bp)
            
        if query_erp and query_erp.isdigit():
            usuarios_activos = usuarios_activos.filter(erp__icontains=query_erp)   
    return render(request, 'buscar_usuario_agregar_indicadores.html', {"usuarios_activos": usuarios_activos, "query_busqueda_usuario": query_busqueda_usuario, "query_bp": query_bp, "query_erp": query_erp})


def agregar_add_indicador(request, usuario_id):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para Evaluar")
        return redirect('login_view')
    
    usuario_que_registra = get_object_or_404(Usuario, id_usuario = request.session['usuario_id'])
    usuario_al_cual_registra = get_object_or_404(Usuario, id_usuario = usuario_id)
    
    if request.method == 'POST':
        comentario = request.POST.get("comentario")
        fecha_creacion = request.POST.get("fecha_creacion")
        fecha_inicio = request.POST.get("fecha_inicio") or None
        fecha_fin = request.POST.get("fecha_fin") or None
        tipo_indicador = request.POST.get("tipo_indicador")
        if usuario_al_cual_registra and usuario_que_registra and comentario and fecha_creacion and tipo_indicador:
            Indicador.objects.create(
            usuario_que_registra = usuario_que_registra,
            usuario_al_cual_registra = usuario_al_cual_registra,
            tipo_indicador = tipo_indicador,
            comentario = comentario,
            fecha_creacion = fecha_creacion,
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin
            )
        return redirect("buscar_usuario_agregar_indicadores")
    return render(request, "add_indicadores_por_usuario_tmp.html", {
        "usuario_al_cual_registra":usuario_al_cual_registra
    })