from sqlalchemy import Column , types
from variables import conexion

class TragoModel(conexion.Model):
    id = Column(type_=types.Integer,
                autoincrement=True,
                primary_key=True)
    nombre = Column(type_=types.Text,
                    nullable=False)
    disponible = Column(type_=types.Boolean,
                        server_default=True)
    
    __tablename__ = 'tragos'