from sqlalchemy import Column , types , ForeignKey , orm
from variables import conexion

class DetallePedido(conexion.Model):
    __tablename__ = 'detalle_pedidos'

    id = Column(type_=types.Integer,
                autoincrement=True,
                primary_key=True)
    cantidad = Column(type_=types.Integer,
                      nullable=False)
    tragoId = Column(ForeignKey(column='tragos.id'),
                   name='trago_id',
                   nullable=False)
    pedidoId  = Column(ForeignKey(column='pedidos.id'),
                    name='pedido_id',nullable=False)
    
    # nombre del modelo  en el cual quiero crear mi relacion virtual
    # Nota: esto no modifica nada mi base de datos
    # Backref > creara un atributo virtual en nuestro modelo en el cual estamos creando una relacion , es decir ahora tendremos en DetallePedido un nuevo atributo llanado 'detallePedidos' que este nos devolvera todo los detalles pedidos
    pedido = orm.relationship('Pedido', backref='detallePedidos')

    trago = orm.relationship('Trago' , backref='tragoPedidos')