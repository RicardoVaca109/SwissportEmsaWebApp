from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from usuarios.models import Usuario
from evaluaciones.models import Evaluacion

def navegacion_dashboard_evaluaciones(request):
    return render(request, 'dashboard_evaluaciones.html')

def look_buscar_empleado(request):  # Buscar un empleado antes de evaluarlo
    query_busqueda_empleado = request.GET.get('q','').strip()
    query_bp = request.GET.get('bp', '').strip()
    
    empleados = Usuario.objects.filter(estatus = 'Activo')
    
    if query_busqueda_empleado:
        empleados = empleados.filter(
            nombre__icontains = query_busqueda_empleado
            ) | empleados.filter(
                apellido__icontains = query_busqueda_empleado) 
            
    if query_bp.isdigit():
        empleados = empleados.filter(bp__icontains=query_bp)
        
    return render(request, 'buscar_empleado.html', {"empleados": empleados, "query_busqueda_empleado": query_busqueda_empleado, "query_bp": query_bp})


def evaluate_evaluar_empleado(request, usuario_id, tipo_evaluacion): # Evaluar al empleado encontrado en Teórica y Práctica
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
        
        messages.success(request, "Evaluación guardada correctamente.")
        return redirect("buscar_empleado")
    
    return render(request, "pruebas_empleado.html", {
        "usuario_calificado": usuario_calificado,
        "tipo_evaluacion": tipo_evaluacion
    })
