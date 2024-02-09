from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

def validar_invitado(funcion):

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        # valida que tengamos un jwt en nuestro request y si hay lo devuelve
         data = verify_jwt_in_request()


         tipo = data[1].get('tipo')

         if not tipo:
              raise NoAuthorizationError('Token invalido')

         if tipo != 'Invitado':
              raise NoAuthorizationError('Usuario con permisos insuficientes')
         
         # si el usuario si es un invitado

         return funcion(*args , **kwargs)
    
    # sirve para indicar al decorador  que la funcion  que utilizara  es el wrapper
    return wrapper

def validar_barman(funcion):

    @wraps(funcion)
    def wrapper(*args, **kwargs):

         data = verify_jwt_in_request()

         
         tipo = data[1].get('tipo')

         if not tipo:
              raise NoAuthorizationError('Token invalido')

         if tipo != 'Barman':
              raise NoAuthorizationError('Usuario con permisos insuficientes')
         
         # si el usuario si es un invitado

         return funcion(*args , **kwargs)

    return wrapper