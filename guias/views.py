from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from guias.models import Guia
from guias.models import Calificacion_Guia
from usuarios.models import Usuario

def navegacion_dashboard_guias(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para ver tus calificaciones")
        return redirect('login_view')

    usuario_actual = get_object_or_404(Usuario, id_usuario=request.session['usuario_id'])
    calificaciones = Calificacion_Guia.objects.filter(usuario_calificador=usuario_actual)

    return render(request, 'dashboard_guias.html', {
        'calificaciones': calificaciones
    })

def agregar_add_calificacion_guia(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes Iniciar Sesión para Evaluar")
        return redirect('login_view')

    usuario_calificador = get_object_or_404(Usuario, id_usuario=request.session['usuario_id'])
    guias_totales = Guia.objects.all()

    if request.method == 'POST':
        guia_id = request.POST.get('id_guia')
        calificacion = request.POST.get('calificacion')
        observacion = request.POST.get('observacion')
        fecha_calificacion = request.POST.get('fecha_calificacion')

        # Validar que los datos no estén vacíos
        if not guia_id or not calificacion or not observacion or not fecha_calificacion:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('dashboard_guias')

        try:
            guia = get_object_or_404(Guia, pk=guia_id)
            calificacion = int(calificacion)
            Calificacion_Guia.objects.create(
                guia=guia,
                usuario_calificador=usuario_calificador,
                calificacion=calificacion,
                observacion=observacion,
                fecha_calificacion=fecha_calificacion
            )
            return redirect('dashboard_guias')

        except ValueError:
            messages.error(request, "Error en los datos ingresados.")
            return redirect('dashboard_guias')

    return render(request, 'add_calificacion_guias.html', {'guias': guias_totales})
        