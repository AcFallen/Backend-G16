# aca estaran declaradas todas las rutas relacionadas ala aplicacion de gestion
from django.urls import path
from .views import mostrarRecetas, vistaPrueba , controlladorInicial
urlpatterns = [
    path('prueba/', view=vistaPrueba),
    path('mostrar-recetas/' , view=mostrarRecetas),
    path('prueba-drf/', view=controlladorInicial)
]