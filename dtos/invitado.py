from marshmallow import Schema , fields , validate

class RegistrarInvitadoDTO(Schema):
    # Validamos que el dni sea entre 8 y 11 digitos
    dni = fields.String(required=True,
                        validate=validate.Regexp(regex ='^(?:\d{8}|\d{11})$',
                                                 error='El dni tiene que tener 8 caracteres y todos deben ser numeros'),
                        error_messages={
                            'required': 'El dni es obligatorio',
                            'null': '', # Este mensaje se muestra cuando el campo no puede ser nulo
                            'validator_failed': ''
                        })
    telefono = fields.String(required=True,
                        validate=validate.Regexp(regex='^\d{9}$',
                                                 error='El telefono tiene que tener 9 digitos'),
                        error_messages={
                            'required' : 'El telefono es obligatorio'
                        })
    
class LoginInvitadoDTO(Schema):
    dni = fields.String(required=True,
                        validate=validate.Regexp(regex ='^(?:\d{8}|\d{11})$',
                                                 error='El dni tiene que tener 8 caracteres y todos deben ser numeros'),
                        error_messages={
                            'required': 'El dni es obligatorio',
                            'null': '', # Este mensaje se muestra cuando el campo no puede ser nulo
                            'validator_failed': ''
                        })