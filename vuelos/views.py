from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from vuelos.models import Vuelo
from aeropuertos.models import Aeropuerto
from aeronave.models import Aeronave

def navegacion_dashboard_vuelos(request):
    total_vuelos = Vuelo.objects.all()
    return render(request, 'dashboard_vuelos.html', {'total_vuelos':total_vuelos}) 

def agregar_add_vuelos(request):
    
    # Obtain total airports / Obtener total aeropuertos 
    total_aeropuertos = Aeropuerto.objects.all()
    # Obtain total airplanes / Obtener total aviones
    total_aeronaves = Aeronave.objects.all()

    if request.method == 'POST':
        fecha_vuelo = request.POST.get('fecha_vuelo')
        codigo_del_vuelo = request.POST.get('codigo_del_vuelo').upper()
        origen_vuelo = request.POST.get('origen_vuelo')
        destino_vuelo = request.POST.get('destino_vuelo')
        escala_intermedia = request.POST.get('escala_intermedia') or None
        aeronave = request.POST.get('aeronave')
        hora_llegada = request.POST.get ('hora_llegada')
        hora_salida = request.POST.get ('hora_salida')
        
        if fecha_vuelo and codigo_del_vuelo and origen_vuelo and destino_vuelo and aeronave and hora_salida and hora_llegada:
            Vuelo.objects.create(
                fecha_vuelo = fecha_vuelo,
                codigo_del_vuelo = codigo_del_vuelo,
                origen_vuelo  = Aeropuerto.objects.get(pk = origen_vuelo),
                destino_vuelo= Aeropuerto.objects.get(pk = destino_vuelo),
                escala_intermedia = Aeropuerto.objects.get(pk = escala_intermedia) if escala_intermedia else None,
                aeronave = Aeronave.objects.get(pk = aeronave),
                hora_salida = hora_salida,
                hora_llegada = hora_llegada
            )
        return redirect(reverse('dashboard_vuelos'))
    return render(request, 'add_vuelos_tmp.html', {'total_aeropuertos':total_aeropuertos, 'total_aeronaves':total_aeronaves})

def editar_edit_vuelos(request, id_vuelo):
    
    vuelo = get_object_or_404(Vuelo, id_vuelo = id_vuelo)
    
    #Obtain all Airports / Obtener todo los aeropuertos
    total_aeropuertos = Aeropuerto.objects.all()
    # Obtain all Aeronaves / Obtener todas las aeronaves
    total_aeronaves = Aeronave.objects.all()
    
    if request.method == 'POST':
        vuelo.fecha_vuelo = request.POST.get('fecha_vuelo')
        vuelo.codigo_del_vuelo = request.POST.get('codigo_del_vuelo').upper()
        vuelo.origen_vuelo = Aeropuerto.objects.get(pk = request.POST.get('origen_vuelo'))
        vuelo.destino_vuelo = Aeropuerto.objects.get(pk = request.POST.get('destino_vuelo'))
        escala_intermedia_id = request.POST.get('escala_intermedia') or None
        vuelo.escala_intermedia = Aeropuerto.objects.get(pk = escala_intermedia_id) if escala_intermedia_id else None
        vuelo.aeronave = Aeronave.objects.get(pk = request.POST.get('aeronave'))
        vuelo.hora_salida = request.POST.get ('hora_salida')
        vuelo.hora_llegada = request.POST.get('hora_llegada')
        vuelo.save()
        return redirect(reverse('dashboard_vuelos'))
    return render(request, 'edit_vuelos_tmp.html',{
        'vuelo' : vuelo,
        'total_aeropuertos' : total_aeropuertos,
        'total_aeronaves' : total_aeronaves,
    })
        
        