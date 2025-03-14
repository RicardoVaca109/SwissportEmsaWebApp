from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from atrasos.models import Atraso
from vuelos.models import Vuelo
from usuarios.models import Usuario

def navegacion_dashboard_atrasos(request):
    total_atrasos = Atraso.objects.all().order_by('id_atraso')
    return render(request, 'dashboard_atrasos.html', {'total_atrasos':total_atrasos})


def look_buscar_vuelo_atrasos(request):
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
        'fecha_vuelo': vuelo.fecha_vuelo.strftime('%Y-%m-%d'),  # Formatear la fecha
        'hora_salida': vuelo.hora_salida.strftime('%H:%M:%S'),
        'hora_llegada': vuelo.hora_llegada.strftime('%H:%M:%S'),
    } for vuelo in vuelos]
    
    return JsonResponse({'vuelos': vuelos_json})


def agregar_add_atrasos(request):
    # Vuelos totales 
    total_vuelos = Vuelo.objects.all()
    
    if request.method == 'POST':
        vuelo = request.POST.get('id_vuelo')
        fecha_atraso = request.POST.get('fecha_atraso')
        codigo_atraso = request.POST.get('codigo_atraso').upper()
        minutos = request.POST.get('minutos')
        motivo_atraso = request.POST.get('motivo_atraso')
        
        if vuelo and fecha_atraso and codigo_atraso and minutos and motivo_atraso:
            Atraso.objects.create(
                vuelo  = Vuelo.objects.get(pk = vuelo),
                fecha_atraso = fecha_atraso,
                codigo_atraso = codigo_atraso,
                minutos = minutos,
                motivo_atraso = motivo_atraso          
            )
        return redirect(reverse('dashboard_atrasos'))
    
    return render(request, 'add_atrasos_tmp.html',{
        'total_vuelos':total_vuelos
    })
    
    
def editar_edit_atraso(request, id_atraso):
    atraso = get_object_or_404(Atraso, id_atraso = id_atraso)
    
    #Obtain all Vuelos / Obtener todos los Vuelos
    total_vuelos = Vuelo.objects.all()
    
    if request.method == 'POST':
        atraso.vuelo = Vuelo.objects.get(pk = request.POST.get('id_vuelo'))
        atraso.fecha_atraso =  request.POST.get('fecha_atraso')
        atraso.codigo_atraso = request.POST.get('codigo_atraso').upper()
        atraso.minutos = request.POST.get('minutos')
        atraso.motivo_atraso = request.POST.get('motivo_atraso')
        atraso.save()
        return redirect(reverse('dashboard_atrasos'))
    return render(request, 'edit_atrasos_tmp.html', {
        'atraso':atraso,
        'total_vuelos':total_vuelos,
    })
        