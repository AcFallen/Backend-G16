from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Barman
from marshmallow import Schema , fields 

class RegistrarBarmanDTO(SQLAlchemyAutoSchema):
    class Meta:
        # model sirve para indicar con que modelo se basara para hacer las validaciones coresspondientes
        model = Barman

class LoginBarmanDTO(Schema):
    username = fields.String(required=True,
                        error_messages={
                            'required': 'El username es obligatorio'
                        })
    password = fields.String(required=True,
                        error_messages={
                            'required' : 'El password es obligatorio'
                        })