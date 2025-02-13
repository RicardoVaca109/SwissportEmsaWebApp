from django.shortcuts import render, redirect
from django.urls import reverse
from indicadores.models import Indicador

def navegacion_dashboard_indicadores(request):
    total_indicadores = Indicador.objects.all()
    return render(request, 'dashboard_indicadores.html', {'total_indicadores':total_indicadores})
