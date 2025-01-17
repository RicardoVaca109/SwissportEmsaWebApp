from django.shortcuts import render
from website.models import Aeropuerto

def navegacion_dashboard_aeropuertos(request):
    total_aeropuertos = Aeropuerto.objects.all
    return render(request, 'dashboard_aeropuertos.html', {'total_aeropuertos':total_aeropuertos})
