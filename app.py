from flask import Flask , request
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel
from flask_migrate import Migrate
from datetime import datetime
from marshmallow import Schema , fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)

# Inicializar la conexion a nuetra BD
# al momento de pasarle la aplicacion de flask en esta se encontrara la cadena de conexion ala bd

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'

conexion.init_app(app)

# Migrate sirve para registrar los cambios en nuestra base de datos realizados desde el ORM

Migrate(app=app , db=conexion)

# @app.before_request
# def inicializacion():

#     conexion.create_all()

class UsuarioDTO(Schema):
    nombre = fields.Str(required = True)
    apellido = fields.Str()
    correo = fields.Email(required = True)
    fechaNacimiento = fields.Date()
    sexo = fields.Str()

class UsuarioModelDto(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel

@app.route('/usuarios', methods=['GET'])
def gestionUsuarios():
    # Select * from Usuarios
    resultado = conexion.session.query(UsuarioModel).all()
    validador = UsuarioModelDto()

    # con el many = TRUE le indicamos que le pasamos una lista de registros por los que tendra que iterar y convertir 
    usuarios = validador.dump(resultado, many=True)
    # print(resultado[0].nombre)
    # usuarios = []
    # for usuario in resultado:
    #     usuarios.append({
    #         'id': usuario.id,
    #         'nombre' : usuario.nombre,
    #         'apellido' : usuario.apellido,
    #         'correo' : usuario.correo,
    #         'fechaNacimiento' : datetime.strftime(usuario.fechaNacimiento,'%Y-%m-%d'),
    #         'sexo' : usuario.sexo
            
    #     })
    
    # print(usuarios)

    return {
        'content' : usuarios
    }, 200

@app.route('/usuario', methods = ['POST'])
def crearUsuario():

    try:
        # Capturar la informacion 
        data = request.get_json()

        # validador = UsuarioDTO()
        validador = UsuarioModelDto()

        dataValidada = validador.load(data)

        nuevoUsuario = UsuarioModel(**dataValidada)
        # Agregar este nuevo registro ala base de datos de manera temporal
        conexion.session.add(nuevoUsuario)

        conexion.session.commit()

        # Sirve para convertir una instancia de la clase a un diccionario para poder devolverlo
        usuarioCreado = validador.dump(nuevoUsuario)

        # Aqui podemos retornar el usuario creado
        # ---------------------------------------
        return {
            'message' : 'Usuario creado',
            'content' : usuarioCreado
        }, 201
    
    except Exception as error:
        return{
            'message' : 'Error al crear usuario',
            'content' : error.args
        }, 400
    
@app.route('/usuario/<int:id>', methods = ['GET' , 'PUT' , 'DELETE'])
def gestionarUsuario(id):
    if request.method == 'GET':
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        validador = UsuarioModelDto()
        usuarioValidado = validador.dump(usuarioEncontrado)
        

        if usuarioEncontrado is None:
            return {
                'message' : 'El usuario no Existe'
            }, 404
        else:
            return{
                'content' : usuarioValidado
            },200
    elif request.method == 'PUT':
        usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id = id).first()
        # si no existe el usuario
        if not usuarioEncontrado:
            return {
                'message' : 'Usuario no existe'
            }, 404
        
        # Si existe el usuario
        validador = UsuarioModelDto()
        # validamos si la informacion enviada es la correcta
        dataValidada = validador.load(request.get_json())
        # query
        conexion.session.query(UsuarioModel).filter_by(id=id).update(dataValidada)
        # guardamos los datos de manera permanente
        conexion.session.commit()
        return {
            'message' : 'Usuario actualizado exitosamente'
        },200
    
    elif request.method == 'DELETE':
        usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id = id).first()
        # si no existe el usuario
        if not usuarioEncontrado:
            return {
                'message' : 'Usuario no existe'
            }, 404
        
        conexion.session.query(UsuarioModel).filter_by(id=id).delete()

        conexion.session.commit()

        return {}, 204

@app.route('/usuario/deshabilitar/<int:id>' , methods = ['DELETE'])
def deshabilitarUsuario(id):
    usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id = id).first()
        # si no existe el usuario
    if not usuarioEncontrado:
        return {
            'message' : 'Usuario no existe'
        }, 404
    
    conexion.session.query(UsuarioModel).filter_by(id=id).update({'activo' : False})

    conexion.session.commit()

    return {
        'message' : 'Usuario inhabilitado exitosamente'
    } , 204

@app.route('/')
def inicial():
    return{
        'message':'bienvenido a mi Api de Usuarios'
    }


if __name__ == '__main__':
    app.run(debug=True)