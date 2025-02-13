from django.shortcuts import render, redirect
from django.urls import reverse
from guias.models import Guia

def navegacion_dashboard_guias(request):
    total_guias = Guia.objects.all()
    return render(request, 'dashboard_guias.html', {'total_guias':total_guias} )
