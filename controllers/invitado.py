from flask_restful import Resource , request
from dtos import RegistrarInvitadoDTO ,LoginInvitadoDTO
from requests import get
from os import environ
from variables import conexion
from models import Invitado
from flask_jwt_extended import create_access_token

class InvitadosController(Resource):


    def post(self):
        dto = RegistrarInvitadoDTO()
        try:
            data_serializada = dto.load(request.get_json())
            print(data_serializada)
            token_api_dni= environ.get('API_DNI')

            if not token_api_dni:

                raise Exception('Falta configurar la token de Api Peru')

            resultado = get(f"https://api.apis.net.pe/v2/reniec/dni?numero={data_serializada.get('dni')}",
                 headers={'Authorization' : f'Bearer {token_api_dni}'})
            
            # convierte la informacion a un diccionario legible en python
            print(resultado.json())
            data_api = resultado.json()

            nuevo_invitado = Invitado(dni = data_serializada.get('dni'),
                     nombre= data_api.get('nombres'),
                     apellido=data_api.get('apellidoPaterno')
                     + ' ' +
                     data_api.get('apellidoMaterno'),
                     telefono= data_serializada.get('telefono'))
            
            conexion.session.add(nuevo_invitado)
            conexion.session.commit()

            return {
                'message' : 'invitado creado exitosamente'                
            }
        except Exception as e:
            return {
                'message': 'Error al crear el invitado',
                'content': e.args
            }
        
class LoginInvitadoController(Resource):
    def post(self):
        dto = LoginInvitadoDTO()
        try:

            data_validada = dto.load(request.get_json())
            invitado_encontrado = conexion.session.query(Invitado).with_entities(Invitado.id).filter_by(dni = data_validada.get('dni')).first()

            if not invitado_encontrado:
                return{
                    'message' : 'Invitado no existe , prueba con el DNI de tu acompanante'
                }, 404
            token = create_access_token(identity=invitado_encontrado[0])
            return {
                'message' : 'Bienvenido',
                'token': token 

            }
        except Exception as e:
            return {
                'message' : 'Error al hacer el login',
                'content' : e.args
            }, 400
