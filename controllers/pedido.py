from flask_restful import Resource , request
from models import Pedido , DetallePedido , Trago
from flask_jwt_extended import get_jwt_identity , jwt_required , get_jwt
from decoradores import validar_invitado , validar_barman
from dtos import CrearPedidoDTO , ListarPedidosDTO
from variables import conexion

class PedidosController(Resource):

    # cuando  queremos que un controlador  requiera de manera obligatoria una token
    # @jwt_required()
    @validar_invitado
    def post(self):
        identity = get_jwt_identity()
        # esto devuelve el payload y dentro de ella todas sus propiedades
        get_jwt()
        dto = CrearPedidoDTO()
        try:
            data_validada = dto.load(request.get_json())
            print(data_validada)
            with conexion.session.begin() as transaccion:
                nuevo_pedido = Pedido(invitado = identity)
                conexion.session.add(nuevo_pedido)

                for detalle in data_validada.get('detalle'):

                    trago_existente = conexion.session.query(Trago).filter_by(id=detalle.get('tragoId')).first()

                    if not trago_existente:
                        raise Exception('El trago no existe')

                    nuevo_detalle_pedido = DetallePedido(cantidad = detalle.get('cantidad'),
                                                        trago = detalle.get('tragoId'),
                                                        pedido = nuevo_pedido.id)
                    conexion.session.add(nuevo_detalle_pedido)

                transaccion.commit()
            return {
                'message' : ''
            }
        except Exception as e:
            # Si algo falla, todo queda obsoleto
            conexion.session.rollback()
            return {
                'message' : 'Error al crear el pedido',
                'content' : e.args
            },400
        
    
    @validar_barman
    def get(self):
        '''
        file: controllers/devolverPedidos.yml
        '''
        pedidos = conexion.session.query(Pedido).all()
        print(pedidos[0].detallePedidos)
        dto = ListarPedidosDTO()
        # DUMP para transformar las instancias a diccionarios
        # many > indicar que pasaremos una lista de instancias por lo que tendra que iterar y transformar cada una de ellas
        resultado = dto.dump(pedidos, many=True)
        
        return {
            'content' : resultado
        }, 200
