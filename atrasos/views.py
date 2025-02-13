from django.shortcuts import render, redirect
from django.urls import reverse
from atrasos.models import Atraso

def navegacion_dashboard_atrasos(request):
    total_atrasos = Atraso.objects.all()
    return render(request, 'dashboard_atrasos.html', {'total_atrasos':total_atrasos})

def agregar_add_atrasos(request):
    return render(request, 'add_atrasos_tmp.html')