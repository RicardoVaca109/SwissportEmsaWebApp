from django.shortcuts import render, redirect
from django.urls import reverse
from accesos.models import Acceso
from usuarios.models import Role
from usuarios.models import Usuario


def navegacion_dashboard_accesos(request):
    # Filtrar usuarios con rol 'Empelado'
    rol_empleado = Role.objects.get(nombre_rol = "Empleado")
    
    usuarios_empleados = Usuario.objects.filter(id_rol = rol_empleado) # Filtra usuarios con rol 'Empleado'
    
    accesos_empleados = Acceso.objects.filter(id_usuario__in = usuarios_empleados)
    return render(request, 'dashboard_accesos.html', {'accesos_empleados': accesos_empleados})

def agregar_add_accesos(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        tipo_accesos = request.POST.get('tipo_accesos')
        identificacion_unica = request.POST.get('identificacion_unica')
        fecha_iniciacion = request.POST.get('fecha_iniciacion')
        fecha_de_baja = request.POST.get('fecha_de_baja', None)

        # Validación básica: verifica que los datos esenciales estén completos
        if id_usuario and tipo_accesos and identificacion_unica and fecha_iniciacion:
            Acceso.objects.create(
                id_usuario=Usuario.objects.get(id_usuario=id_usuario),  # Obtén el usuario con la ID dada
                tipo_accesos=tipo_accesos,
                identificacion_unica=identificacion_unica,
                fecha_iniciacion=fecha_iniciacion,
                fecha_de_baja=fecha_de_baja if fecha_de_baja else None,  # Permitir que sea opcional
            )
            return redirect(reverse('dashboard_accesos'))
    
    # Si el método es GET, mostrar el formulario con usuarios de rol "Empleado"
    rol_empleado = Role.objects.get(nombre_rol="Empleado")
    usuarios_empleados = Usuario.objects.filter(id_rol=rol_empleado)
    return render(request, 'add_accesos_tmp.html', {'usuarios_empleados': usuarios_empleados})