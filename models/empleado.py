from variables import conexion
from sqlalchemy import Column , types , ForeignKey

class EmpleadoModel(conexion.Model):
    id = Column(type_=types.INTEGER , 
                autoincrement=True, 
                primary_key=True)
    nombre = Column(type_=types.String(20) , nullable=False)
    apellido = Column(type_=types.String(20) , nullable=False)
    email = Column(type_=types.String(40) , nullable=False , unique=True)

    areaId = Column(ForeignKey(column='areas.id'),
                    nullable=False)
    
    __tablename__ = 'empleados'