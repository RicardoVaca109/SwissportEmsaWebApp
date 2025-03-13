from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.http import JsonResponse
from eventos.models import Evento
from vuelos.models import Vuelo
from usuarios.models import Usuario
from aeropuertos.models import Aeropuerto

def navegacion_dashboard_eventos(request):
    total_eventos = Evento.objects.all().order_by('id_evento')
    return render(request, 'dashboard_eventos.html', {'total_eventos':total_eventos} )


def look_buscar_usuario_eventos(request):
    query_busqueda_usuario = request.GET.get('q', '').strip()
    
    usuarios_activos = Usuario.objects.filter(estatus='Activo')
    
    if query_busqueda_usuario:
        usuarios_activos = usuarios_activos.filter(
            Q(nombre__icontains=query_busqueda_usuario) |
            Q(apellido__icontains=query_busqueda_usuario)
        )
    
    # Convertir los resultados a un formato que pueda ser enviado como JSON
    usuarios_json = [{
        'id_usuario': usuario.id_usuario,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido
    } for usuario in usuarios_activos]
    
    return JsonResponse({'usuarios_activos': usuarios_json})


def look_buscar_vuelo_eventos(request):
    query_busqueda_vuelo = request.GET.get('q', '').strip()
    
    vuelos = Vuelo.objects.all()
    
    if query_busqueda_vuelo:
        vuelos = vuelos.filter(codigo_del_vuelo__icontains=query_busqueda_vuelo)
    
    # Convertir los resultados a un formato que pueda ser enviado como JSON
    vuelos_json = [{
        'id_vuelo': vuelo.id_vuelo,
        'codigo_del_vuelo': vuelo.codigo_del_vuelo,
        'origen_vuelo': vuelo.origen_vuelo.estacion_aeropuerto,
        'destino_vuelo': vuelo.destino_vuelo.estacion_aeropuerto,
        'fecha_vuelo': vuelo.fecha_vuelo.strftime('%Y-%m-%d'),# Formatear la fecha
        'hora_salida': vuelo.hora_salida.strftime('%H:%M:%S'),
        'hora_llegada': vuelo.hora_llegada.strftime('%H:%M:%S'),
    } for vuelo in vuelos]
    
    return JsonResponse({'vuelos': vuelos_json})


def agregar_add_eventos(request):
    # Vuelos totales 
    total_vuelos = Vuelo.objects.all()
    # Usuarios totales
    total_usuarios = Usuario.objects.all()
    
    if request.method == 'POST':
        vuelo = request.POST.get('id_vuelo')
        fecha_evento = request.POST.get('fecha_evento')
        evento_lir = request.POST.get('evento_lir') 
        evento_pax = request.POST.get('evento_pax') 
        motivo = request.POST.get('motivo')
        tipo_evento = request.POST.get('tipo_evento')
        plan_de_accion = request.POST.get('plan_de_accion')
        usuario_involucrado = request.POST.get('usuario_involucrado')
    

        if vuelo and fecha_evento and evento_lir and evento_pax and motivo and tipo_evento and plan_de_accion and usuario_involucrado:
            Evento.objects.create(
                vuelo  = Vuelo.objects.get(pk = vuelo),
                usuario_involucrado = Usuario.objects.get(pk = usuario_involucrado),
                fecha_evento = fecha_evento,
                evento_lir = evento_lir,
                evento_pax = evento_pax,
                motivo = motivo,
                tipo_evento = tipo_evento,
                plan_de_accion = plan_de_accion,
            )
            return redirect(reverse('dashboard_eventos'))
    return render(request, "add_eventos_tmp.html", {"total_vuelos": total_vuelos, "total_usuarios": total_usuarios})


def editar_edit_evento(request, id_evento):
    evento = get_object_or_404(Evento, id_evento = id_evento)
    
    # Vuelos totales 
    total_vuelos = Vuelo.objects.all()
    # Usuarios totales
    total_usuarios = Usuario.objects.all()
    
    if request.method == 'POST':
        evento.vuelo = Vuelo.objects.get(pk = request.POST.get('id_vuelo'))
        evento.usuario_involucrado = Usuario.objects.get(pk = request.POST.get('usuario_involucrado'))
        evento.fecha_evento = request.POST.get('fecha_evento')
        evento.evento_lir = request.POST.get('evento_lir') 
        evento.evento_pax = request.POST.get('evento_pax')
        evento.motivo = request.POST.get('motivo') 
        evento.tipo_evento = request.POST.get('tipo_evento')
        evento.plan_de_accion = request.POST.get('plan_de_accion')
        evento.save()
        return redirect(reverse('dashboard_eventos'))
    return render(request, 'edit_eventos_tmp.html', {
        'evento':evento,
        'total_vuelos':total_vuelos,
        'total_usuarios':total_usuarios,       
    })
        
        
    
    