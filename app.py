from flask import Flask
from flask_migrate import Migrate
from variables import conexion
from dotenv import load_dotenv
# os > operating systemc
from os import environ
#tablas
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager

from datetime import timedelta

# leera el archivo .env si existe y agregara todas las variables como si fuesen variables de entorno del sistema
# este load_dotenv teine que ir en la parte mas alta para que pueda ser utilizado en todo el proyecto
load_dotenv()

app = Flask(__name__)
api = Api(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Configuraciones para mi JWT
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1 , minutes=30)

conexion.init_app(app)

JWTManager(app=app)

# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app , db=conexion)

# Agrego mis rutas
api.add_resource(InvitadosController, '/invitados')
api.add_resource(BarmanController, '/barman')
api.add_resource(LoginController, '/login')
api.add_resource(LoginInvitadoController, '/login-invitado')
api.add_resource(PedidosController, '/pedidos')


if __name__ == '__main__':
    app.run(debug=True)