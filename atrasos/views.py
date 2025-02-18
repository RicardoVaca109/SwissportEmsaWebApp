from django.shortcuts import render, redirect
from django.urls import reverse
from atrasos.models import Atraso
from vuelos.models import Vuelo

def navegacion_dashboard_atrasos(request):
    total_atrasos = Atraso.objects.all()
    return render(request, 'dashboard_atrasos.html', {'total_atrasos':total_atrasos})

def agregar_add_atrasos(request):
    # Vuelos totales 
    total_vuelos = Vuelo.objects.all()
    if request.method == 'POST':
        vuelo = request.POST.get('id_vuelo')
        fecha_atraso = request.POST.get('fecha_atraso')
        codigo_atraso = request.POST.get('codigo_atraso')
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