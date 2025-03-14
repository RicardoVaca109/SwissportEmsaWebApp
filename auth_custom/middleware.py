from django.shortcuts import redirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        rutas_permitidas_sin_sesion = [
            reverse('login_view'),
            reverse('logout_view'),
        ]
        if request.path not in rutas_permitidas_sin_sesion and 'usuario_id' not in request.session:
            return redirect('login_view')
        
        return self.get_response(request)