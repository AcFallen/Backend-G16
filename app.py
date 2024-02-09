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
from flask_jwt_extended import JWTManager , get_jwt_identity

from datetime import timedelta

from decoradores import validar_barman
from models.pedido import EstadoPedidosEnum

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

@app.route('/preparar-pedido/<int:id>' , methods=['POST'])
@validar_barman
def prepararPedido(id):
    barmanId = get_jwt_identity()

    # Primero buscar si el pedido existe con ese id
    pedido_encontrado = conexion.session.query(Pedido).filter(Pedido.id == id , Pedido.barmanId == None).first()

    if not pedido_encontrado:
        return{
            'message' : 'El pedido a buscar no existe  o ya fue tomado'
        }, 400
    
    # actualizar el pedido y configurar el barman y cambiar el estado a 'PREPARANDO'
    conexion.session.query(Pedido).filter_by(id = pedido_encontrado.id).update({ Pedido.barmanId: barmanId ,
                                                                                 Pedido.estado: EstadoPedidosEnum.PREPARANDO})
    conexion.session.commit()
    return {
        'message': 'Pedido configurado exitosamente'
    }

@app.route('/pedido-preparado/<int:id>', methods = ['POST'])
@validar_barman
def pedidoPreparado(id):
    barmanId = get_jwt_identity()
    pedido_encontrado = conexion.session.query(Pedido).filter(Pedido.id == id , 
                                                              Pedido.barmanId == barmanId,
                                                              Pedido.estado == EstadoPedidosEnum.PREPARANDO).first()

    if not pedido_encontrado:
        return{
            'message' : 'El pedido a buscar no existe  no tienes los permisos necesarios'
        }, 400
    
    conexion.session.query(Pedido).filter(Pedido.id == id).update({Pedido.estado:EstadoPedidosEnum.PREPARADO})

    conexion.session.commit()

    return{
        'message':'Pedido completado'
    },200

if __name__ == '__main__':
    app.run(debug=True)