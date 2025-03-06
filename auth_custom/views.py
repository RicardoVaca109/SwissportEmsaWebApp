from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from usuarios.models import Usuario

def auth_login_view(request): 
    if request.method == "POST":
        email = request.POST.get('email', '').strip().lower()
        contrasenia = request.POST.get('contrasenia',  '')
        if email:  
            try:
                    usuario = Usuario.objects.get(email=email, estatus="Activo") # Buscar usuario por email
                    if check_password(contrasenia, usuario.contrasenia):  # Verificar contraseña 
                        request.session['usuario_id'] = usuario.id_usuario  # Guardar en sesión
                        request.session['usuario_nombre'] = usuario.nombre
                        request.session['usuario_rol'] = usuario.rol.nombre_rol
                        
                        redirecciones_por_rol = [
                            {
                                "roles" : ["KAM","KAM Nacional","Supervisor"],
                                "condicion": lambda usuario_validar_rol: usuario_validar_rol.bp is not None,
                                "url": "dashboard_accesos"                           
                            },
                            {
                                "roles" : ["OJT"],
                                "condicion": lambda usuario_validar_rol: True,
                                "url": "dashboard_rol_ojt"                                
                            },
                        ]
                        
                        for regla in redirecciones_por_rol:
                            if usuario.rol.nombre_rol in regla["roles"] and regla["condicion"](usuario):
                                
                                return redirect(regla["url"])
                            
                        return redirect("dashboard_general")
                    else:
                        messages.error(request, "Contraseña incorrecta")
            except Usuario.DoesNotExist:
                    messages.error(request, "Usuario no encontrado o Usuario Inactivo")

    return render(request, "initial_login.html")

def auth_logout_view(request):
    logout(request)  # Eliminar sesión
    return redirect("login_view")  # Redirigir al login
