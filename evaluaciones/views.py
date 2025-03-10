from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from usuarios.models import Usuario
from evaluaciones.models import Evaluacion

def navegacion_dashboard_evaluaciones(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para ver tus evaluaciones")
        return redirect('login_view')
    usuario_que_califica_en_sesion = get_object_or_404(Usuario, id_usuario=request.session['usuario_id'])
    evaluaciones_calificadas_por_usuario = Evaluacion.objects.filter(usuario_que_califica = usuario_que_califica_en_sesion)
    
    return render(request, 'evaluaciones_realizadas_tmp.html', {
        'evaluaciones_calificadas_por_usuario':evaluaciones_calificadas_por_usuario
    })

def look_buscar_usuario_evaluaciones(request):  # Buscar un empleado antes de evaluarlo
    query_busqueda_usuario = request.GET.get('q','').strip()
    query_bp = request.GET.get('bp', '').strip()
    
    usuarios_activos = None   # Inicialmente, no se carga ningún empleado
    
    if query_busqueda_usuario or (query_bp and query_bp.isdigit()): # Solo buscar si hay un criterio
        usuarios_activos = Usuario.objects.filter(estatus='Activo') 
    
        if query_busqueda_usuario:
            usuarios_activos = usuarios_activos.filter(
                nombre__icontains = query_busqueda_usuario
                ) | usuarios_activos.filter(
                    apellido__icontains = query_busqueda_usuario) 
                
        if query_bp and query_bp.isdigit():
            usuarios_activos = usuarios_activos.filter(bp__icontains=query_bp)   
    return render(request, 'buscar_usuario_evaluaciones.html', {"usuarios_activos": usuarios_activos, "query_busqueda_usuario": query_busqueda_usuario, "query_bp": query_bp})


def evaluate_evaluar_usuario(request, usuario_id, tipo_evaluacion): # Evaluar al empleado encontrado en Teórica y Práctica
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para Evaluar")
        return redirect('login_view')
    
    usuario_que_califica = get_object_or_404(Usuario, id_usuario = request.session['usuario_id'])
    usuario_calificado = get_object_or_404(Usuario, id_usuario = usuario_id)
    
    if request.method == "POST":
        calificacion = request.POST.get("calificacion")
        observacion = request.POST.get("observacion")
        fecha_calificacion = request.POST.get("fecha_calificacion")
        
        Evaluacion.objects.create(
            usuario_que_califica = usuario_que_califica,
            usuario_calificado = usuario_calificado,
            tipo_evaluacion = tipo_evaluacion,
            calificacion = calificacion,
            observacion = observacion,
            fecha_calificacion = fecha_calificacion
        )
        
        # messages.success(request, "Evaluación guardada correctamente.")
        return redirect("buscar_usuario_evaluaciones")
    
    return render(request, "pruebas_usuario.html", {
        "usuario_calificado": usuario_calificado,
        "tipo_evaluacion": tipo_evaluacion
    })
