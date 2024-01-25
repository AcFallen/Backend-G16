from variables import conexion
from sqlalchemy import Column, types, ForeignKey

class DireccionModel(conexion.Model):
    id = Column(type_=types.INTEGER , 
                autoincrement=True, 
                primary_key=True)
    calle = Column(type_=types.Text)
    numero = Column(type_=types.String(20))
    referencia = Column(type_=types.Text)
    predeterminada = Column (type_=types.Boolean, default=False)

    # Relaciones
    usuarioId = Column(ForeignKey(column='usuarios.id'), 
                       nullable=False , 
                       name='usuario_id')
    __tablename__ = 'direcciones'