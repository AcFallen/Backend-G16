from sqlalchemy import Column , types
from variables import conexion

class UsuarioModel(conexion.Model):
    id = Column(name='id', 
                type_=types.INTEGER, 
                autoincrement=True, 
                primary_key=True)
    nombre = Column(type_= types.String(100), nullable=False)
    apellido = Column(type_=types.String(100))
    fechaNacimiento = Column(name='fecha_nacimiento', type_=types.Date)
    correo = Column(type_=types.String(100),unique=True , nullable= False)
    sexo =  Column(type_=types.String(50), server_default='NINGUNO')
    activo = Column(type_=types.Boolean, server_default='1')

    # Ahora para indicar como queremos que se llame esta tabla en la BD

    __tablename__ = 'usuarios'