from marshmallow import Schema , fields

class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)

class CrearPedidoDTO(Schema):
    detalle = fields.List(fields.Nested(ItemPedidoDTO))