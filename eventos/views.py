from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from eventos.models import Evento
from vuelos.models import Vuelo 
from usuarios.models import Usuario

def navegacion_dashboard_eventos(request):
    total_eventos = Evento.objects.all()
    return render(request, 'dashboard_eventos.html', {'total_eventos':total_eventos} )

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