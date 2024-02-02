from variables import conexion
from sqlalchemy import Column, types

class AreaModel(conexion.Model):
    id = Column(name='id',
                type_=types.Integer,
                autoincrement=True,
                primary_key=True)
    nombre = Column(type_=types.String(100),nullable=False)
    piso = Column(type_=types.String(100),nullable=False)

    __tablename__ = 'areas'