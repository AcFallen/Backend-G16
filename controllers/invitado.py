from flask_restful import Resource

class InvitadosController(Resource):
    def post(self):
        print('ingreso al post')

        return {
            'message' : 'invitado creado exitosamente'
        }