from django.shortcuts import render, redirect
from django.urls import reverse
from eventos.models import Evento

def navegacion_dashboard_eventos(request):
    total_eventos = Evento.objects.all()
    return render(request, 'dashboard_eventos.html', {'total_eventos':total_eventos} )