from marshmallow import Schema , fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Pedido , DetallePedido , Trago
from models.pedido import EstadoPedidosEnum
from marshmallow_enum import EnumField


class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)

class CrearPedidoDTO(Schema):
    detalle = fields.List(fields.Nested(ItemPedidoDTO))

class TragoDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = Trago
        # el atributo fields sirve para indicar que atributos queremos utilizar, los que esten declarados seran los que se muestren
        fields = ['nombre']

class DetallePedidoDTO(SQLAlchemyAutoSchema):

    trago = fields.Nested(nested=TragoDTO , attribute = 'trago')
    
    class Meta:
        model = DetallePedido
        # si queremos mostrar las llaves foraneas de nuestro modelo definimos el atributo include_fk
        # include_fk = True
        fields = ['trago', 'cantidad']

class ListarPedidosDTO(SQLAlchemyAutoSchema):

    # cuando en un modelo tenemos una columna de tipo enum tenemos que indicarle a marshmelow 
    estado = EnumField(EstadoPedidosEnum)
    # si colocamos un nombre diferente al atributo virtual no ara match y por ende no mostrara la informacion, caso contrario si concuerda si mostrara la informacion.
    # en este caso como pedido puede tener muchos detallePEdidos tenemos que colocar el parametro many= True para que los itere
    detallePedidos = fields.Nested(nested=DetallePedidoDTO , many=True)

    class Meta:
        model = Pedido
        # Buscara si este modelo tiene RELATIONSHIPS y si los tiene los agregara al dto
        # include_relationships = True
        
    