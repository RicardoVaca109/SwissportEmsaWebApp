from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from aeropuertos.models import Aeropuerto

def navegacion_dashboard_aeropuertos(request):
    total_aeropuertos = Aeropuerto.objects.all()
    return render(request, 'dashboard_aeropuertos.html', {'total_aeropuertos':total_aeropuertos})

def agregar_add_aeropuertos(request):
    
    if request.method == 'POST':
        estacion_aeropuerto = request.POST.get('estacion_aeropuerto').upper()
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        tipo_aeropuerto = request.POST.get('tipo_aeropuerto')
        
        # Create new register on Database / Crear un nuevo registro en la base de datos
        
        # Validación básica: verifica que los datos estén completos
        if estacion_aeropuerto and nombre and ciudad and pais and tipo_aeropuerto:
            Aeropuerto.objects.create(
                estacion_aeropuerto=estacion_aeropuerto,
                nombre=nombre,
                ciudad=ciudad,
                pais=pais,
                tipo_aeropuerto=tipo_aeropuerto,
            )
            return redirect(reverse('dashboard_aeropuertos'))
    return render(request, 'add_aeropuertos_tmp.html')

def editar_edit_aeropuerto(request, id_aeropuerto):
    aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto = id_aeropuerto)
    if request.method == 'POST':
        aeropuerto.estacion_aeropuerto = request.POST.get('estacion_aeropuerto').upper()
        aeropuerto.nombre = request.POST.get('nombre')
        aeropuerto.ciudad = request.POST.get('ciudad')
        aeropuerto.pais = request.POST.get('pais')
        aeropuerto.tipo_aeropuerto = request.POST.get('tipo_aeropuerto')
        aeropuerto.save()
        return redirect(reverse('dashboard_aeropuertos'))
    return render(request, 'edit_aeropuertos_tmp.html', {'aeropuerto': aeropuerto})


def eliminar_delete_aeropuerto(request, id_aeropuerto):
    aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto = id_aeropuerto)
    if request.method == 'POST':
        aeropuerto.delete()
        return redirect(reverse('dashboard_aeropuertos'))
    return render(request, 'dashboard_aeropuertos.html', {'total_aeropuertos': Aeropuerto.objects.all()})
    