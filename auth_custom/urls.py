from django.urls import path
from auth_custom.views import auth_login_view, auth_logout_view

urlpatterns = [
    path('', auth_login_view, name = 'login_view'),
    path('logout/', auth_logout_view, name = 'logout_view')
]