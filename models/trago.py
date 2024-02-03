from sqlalchemy import Column , types
from variables import conexion

class Trago(conexion.Model):
    id = Column(type_=types.Integer,
                autoincrement=True,
                primary_key=True)
    nombre = Column(type_=types.Text,
                    nullable=False)
    disponible = Column(type_=types.Boolean,
                        server_default='1')
    
    __tablename__ = 'tragos'