from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager


# Create your models here.
TipoPlatoOpciones = [
    ('entrada', 'ENTRADA'),
    ('plato_de_fondo', 'PLATO DE FONDO'),
    ('postre', 'POSTRE')
]

class Plato(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    foto = models.ImageField()
    tipo = models.TextField(choices=TipoPlatoOpciones,
                            default=TipoPlatoOpciones[0][0]) # entrada
    class Meta:
        db_table = 'platos'

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True , null=False)
    descripcion = models.TextField(null=False)
    # TODO: para crear una relacion entre 2 modelos se usa el ForeignKey
    # to  > sirve para indicar la referencia hacia la tabla con la cual crearemos la relacion
    # db_column > indica como se llamara la columna en la base de datos
    # on_delete > indica como se comportara cuando se elimine el padre(Plato al cual pertenece)
    # CASCADE > si se elimina el plato, se eliminaran todos sus ingredientes
    # PROTECT > evita la eliminacion del plato si tiene ingredientes lanzado un error de tipo ProtectedError
    # RESTRICT > evita la eliminacion del plato si tiene ingredientes y lanza un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion del plato y le cambia el valor a sus ingredientes a la columna plato_id a NULL (los deja huerfanos)
    # SET_DEFAULT > permite la eliminacion del plato y cambia el valor de la columna a un valor por defecto
    # DO_NOTHING > permite la eliminacion del plato y no cambia el valor del ingrediente del plato_id generando inconsistencia de datos
    platoId = models.ForeignKey(to=Plato , db_column = 'plato_id', on_delete= models.PROTECT , related_name = 'ingredientes')

    class Meta:
        db_table = 'ingredientes'

class Preparacion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    orden = models.IntegerField(null=False)
    platoId = models.ForeignKey(to=Plato , db_column='plato_id', on_delete = models.PROTECT , related_name ='preparaciones')

    class Meta:
        db_table = 'preparaciones'
        ordering = ['-orden']
        unique_together = [['orden', 'platoId']]


class ManejadorUsuario(BaseUserManager):
    def create_superuser(self, nombre , correo , password):
        if not correo:
            raise ValueError('El usuario tiene que tener un correo')
        
        correo_normalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(correo = correo , nombre = nombre)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser =True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()
# vamos a utilizar el modelo auth_user 
# PERMISSION MIXIN > sirve para indicarle a nuestro proyecto que ahora esta tabla  tbn sera la encargada de manejar el sistema de permisos, es decir ahi se encuentra todos los permisos de nuestra aplicacion en el panel administrativo
class Cheff(AbstractBaseUser , PermissionsMixin):
    id = models.AutoField(primary_key=True , null=False)
    nombre = models.TextField(null=False)
    correo = models.EmailField(unique =True , null=False)
    password = models.TextField(null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)

    # para poder realizar el login en el panel administrativo
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    #TODO: vamos a modificar el comportamiento del atributo objects para que pueda aceptar una creacion de superusario
    objects = ManejadorUsuario()

    class Meta:
        db_table = 'cheffs'