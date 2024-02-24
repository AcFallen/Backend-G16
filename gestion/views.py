from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato , Ingrediente ,Cheff
from .serializers import PlatoSerializer , IngredienteSerializer , PreparacionSerializer , PlatoConIngredientesYPreparacionesSerializer , RegistroCheffSerializer
from rest_framework import status
from os import remove
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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
        serializador = PlatoConIngredientesYPreparacionesSerializer(instance=plato_encontrado)
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
    
class IngredientesController(APIView):
    def post (self,request):
        request.data
        serializador = IngredienteSerializer(data=request.data)
        validacion = serializador.is_valid()

        if validacion:
            serializador.save()
            return Response ({
                'message': 'Ingrediente agregado exitosamente',
                'content': serializador.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al ingresar el ingrediente',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
@api_view(http_method_names=['GET'])
def listarIngredientesPlato(request,id):
    ingrediente_encontrado = Ingrediente.objects.filter(platoId=id).all()
    if not ingrediente_encontrado:
        return Response({
            'message': 'El plato no tiene ingredientes'
        })
    else:
        serializador = IngredienteSerializer(instance=ingrediente_encontrado , many=True)
        return Response ({
            'content': serializador.data
        })


@swagger_auto_schema(method='post',
                     request_body=PreparacionSerializer,
                     responses={
                         201: openapi.Response('respuesta exitosa',
                                               examples={
                                                   'application/json': {
                                                       'message': 'Preparacion agregada con exitosamente al plato',
                                                       'content': {
                                                           'id': 1,
                                                           'descripcion': '',
                                                           'orden': 1,
                                                           'platoId': 10
                                                       }
                                                   }
                                               }),
                         400: openapi.Response('respuesta fallida',
                                               examples={
                                                   'application/json': {
                                                       'message': 'Error al crear la preparacion',
                                                       'content': ' errores'
                                                   }
                                               })})
@api_view(http_method_names=['POST'])
def crearPreparacion(resquest):

    serializador = PreparacionSerializer(data=resquest.data)
    if serializador.is_valid():
        serializador.save()
        return Response(data={
            'message':'Preparacion agregada exitosamente al plato',
            'content': serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            'message': 'Error al crear la preparacion',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', responses={200: openapi.Response(description='recetas', examples={
    'application/json':{
        'content':'platoconingredientesypreparaciones'
    }
},schema=PlatoConIngredientesYPreparacionesSerializer)})    
@api_view(http_method_names=['GET'])
def buscarRecetas(request):
    print(request.query_params)
    if request.query_params.get('nombre'):
        nombre = request.query_params.get('nombre')

        resultado = Plato.objects.filter(nombre__icontains = nombre).all()
        
        serializador = PlatoConIngredientesYPreparacionesSerializer(instance=resultado , many=True)

        print(resultado)
        return Response(data={
            'content': serializador.data
        })
    else:
        return Response(data={
            'message': 'Falta el nombre en el query param'
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['POST'])
def crearCheff(request):
    serializador = RegistroCheffSerializer(data=request.data)
    if serializador.is_valid():
        #serializador.save()
        nuevo_cheff = Cheff(nombre=serializador.validated_data.get('nombre'),
                            correo=serializador.validated_data.get('correo'))
        nuevo_cheff.set_password(serializador.validated_data.get('password'))
        nuevo_cheff.save()
        print(request.data.get('correo'))
        
        return Response(data={
            'message':'cheff creado exitosamente',
            'content': serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            'message':'Error al crear el cheff',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)