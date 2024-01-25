from flask import Flask
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel

app = Flask(__name__)

# Inicializar la conexion a nuetra BD
# al momento de pasarle la aplicacion de flask en esta se encontrara la cadena de conexion ala bd

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'

conexion.init_app(app)

@app.before_request
def inicializacion():
    conexion.create_all()

@app.route('/')
def inicial():
    return{
        'message':'bienvenido a mi Api de Usuarios'
    }


if __name__ == '__main__':
    app.run(debug=True)