from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato
from .serializers import PlatoSerializer
from rest_framework import status
from os import remove


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

class PlatosController(APIView):
    def get(self, request):
        resultado = Plato.objects.all()
        print(resultado)
        #TODO: instance > cuando tenemos instancias del modelo para serializar
        #TODO: data > cuando tenemos informacion que vamos a guardar , modificat en la base de datos
        serializador = PlatoSerializer(instance=resultado , many=True)

        return Response(data={
            'message':'Me hicieron get',
            'content' : serializador.data
        })
    
    def post(self,request):
        print(request.data)
        serializador = PlatoSerializer(data=request.data)
        validacion = serializador.is_valid()
        
        if validacion:
            serializador.save()

            return Response(data={
                'message':'Plato agregado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el plato',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
class PlatoController(APIView):
    def get(self,request,id):
        plato_encontrado = Plato.objects.filter(id = id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        serializador = PlatoSerializer(instance=plato_encontrado)
        return Response(data={
            'content': serializador.data
        })
    
    def put(self,request,id):
        plato_encontrado = Plato.objects.filter(id = id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_antigua = plato_encontrado.foto.path
        
        serializador = PlatoSerializer(data=request.data)

        if serializador.is_valid():

            resultado = serializador.update(instance=plato_encontrado,
                                validated_data=serializador.validated_data)
            print(resultado)

            
            remove(imagen_antigua)
            
            return Response(data={
                'message': 'Plato actualizado exitosamente'
            })

        else:
            return Response(data={
                'message': 'Error al actualziar el plato',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        plato_encontrado = Plato.objects.filter(id = id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        imagen_antigua= plato_encontrado.foto.path

        Plato.objects.filter(id=id).delete()

        remove(imagen_antigua)

        return Response(data=None,status=status.HTTP_204_NO_CONTENT)