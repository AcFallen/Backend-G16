# aca estaran declaradas todas las rutas relacionadas ala aplicacion de gestion
from django.urls import path
from .views import mostrarRecetas, vistaPrueba , controlladorInicial ,PlatosController ,PlatoController
urlpatterns = [
    path('prueba/', view=vistaPrueba),
    path('mostrar-recetas/' , view=mostrarRecetas),
    path('prueba-drf/', view=controlladorInicial),
    path('platos/', view=PlatosController.as_view()),
    path('plato/<int:id>', PlatoController.as_view())
]