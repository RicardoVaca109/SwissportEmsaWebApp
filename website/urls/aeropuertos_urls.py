from django.urls import path
from website.views.aeropuertos_view import navegacion_dashboard_aeropuertos, agregar_add_aeropuertos, eliminar_delete_aeropuerto, editar_edit_aeropuerto


urlpatterns = [
    # Principal Route/ Ruta principal
    path('', navegacion_dashboard_aeropuertos, name = 'dashboard_aeropuertos'),
    path('agregar/', agregar_add_aeropuertos , name = 'add_aeropuertos'),
    path('editar/<int:id_aeropuerto>/', editar_edit_aeropuerto, name = 'edit_aeropuertos' ),
    path('eliminar/<int:id_aeropuerto>/',eliminar_delete_aeropuerto, name = 'delete_aeropuertos')
    ]