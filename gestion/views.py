from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Create your views here.
def vistaPrueba(request):
    usuario = {
        'nombre': 'Roberto',
        'apellido': 'Apaza',
        'hobbies': [
            {
                'descripcion':'jugar'
            },
            {
                'descripcion':'viajar'
            }
        ]
    }
    return render(request=request, template_name='prueba.html' , context=usuario)

def mostrarRecetas(request):

    return render(request , 'mostrarRecetas.html')

# siempre que una funcion trabaja como controlador recibiremos el request (informacion que envia el cliente)
@api_view(http_method_names=['GET','POST'])
def controlladorInicial(request):
    return Response(data = {
        'message': 'Bienvenido a mi API'
    })