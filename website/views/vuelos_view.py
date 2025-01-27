from django.shortcuts import render, redirect
from django.urls import reverse
from website.models import Vuelo
from website.models import Aeropuerto

def navegacion_dashboard_vuelos(request):
    total_vuelos = Vuelo.objects.all()
    return render(request, 'dashboard_vuelos.html', {'total_vuelos':total_vuelos}) 

def agregar_add_vuelos(request):
    
    # Obtain total airports / Obtener total aeropuertos 
    total_aeropuertos = Aeropuerto.objects.all()
    
    if request.method == 'POST':
        fecha_vuelo = request.POST.get('fecha_vuelo')
        codigo_del_vuelo = request.POST.get('codigo_del_vuelo')
        origen_vuelo = request.POST.get('origen_vuelo')
        destino_vuelo = request.POST.get('destino_vuelo')
        
        if fecha_vuelo and codigo_del_vuelo and origen_vuelo and destino_vuelo:
            Vuelo.objects.create(
                fecha_vuelo = fecha_vuelo,
                codigo_del_vuelo = codigo_del_vuelo,
                origen_vuelo  = Aeropuerto.objects.get(pk = origen_vuelo),
                destino_vuelo= Aeropuerto.objects.get(pk = destino_vuelo)
            )
        return redirect(reverse('dashboard_vuelos'))
    return render(request, 'add_vuelos_tmp.html', {'total_aeropuertos':total_aeropuertos})
        