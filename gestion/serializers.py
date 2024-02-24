from rest_framework import serializers
from .models import Plato , Ingrediente , Preparacion , Cheff

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class PreparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparacion
        fields = '__all__'

class PlatoConIngredientesYPreparacionesSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)
    #TODO: si queremos definir un atributo que no existe en nuestro modelos pero queremos utilizar un atributo como referencia entonces podremos source
    pasos = PreparacionSerializer(many=True , source='preparaciones')

    class Meta:
        model = Plato
        fields = '__all__'

class RegistroCheffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cheff
        exclude = ['groups','user_permissions','last_login']
        extra_kwargs = {
            'password':{
                'write_only':True
            },
            'is_staff':{
                'read_only': True
            },
            'is_active':{
                'write_only': True
            }
        }