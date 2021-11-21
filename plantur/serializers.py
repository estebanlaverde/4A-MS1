from rest_framework import serializers 
from .models import Usuario, Hoteles, Proveedor, Ciudades, Transporte, Actividad, Factura, Plan


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    ciudad_Act = CiudadesSerializer(read_only=True)  #SERIALIZER_ANIDADO

    class Meta:
        model = Actividad
        fields = '__all__'

class HotelesSerializer(serializers.ModelSerializer):
    ciudad_hotel = CiudadesSerializer(read_only=True)  #SERIALIZER_ANIDADO

    class Meta:
        model = Hoteles
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    ciudad_Prov = CiudadesSerializer(read_only=True)  #SERIALIZER_ANIDADO
    actividad = ActividadSerializer(read_only=True)

    class Meta:
        model = Proveedor
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    ciudad_Transp = CiudadesSerializer(read_only=True)  #SERIALIZER_ANIDADO

    class Meta:
        model = Transporte
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    actividad = ActividadSerializer(read_only=True)  #SERIALIZER_ANIDADO
    ciudad_Plan = CiudadesSerializer(read_only=True)
    cedula = UsuarioSerializer(read_only=True)
    nit_hotel = HotelesSerializer(read_only=True)
    nit_proveedor = ProveedorSerializer(read_only=True)
    nit_transporte = TransporteSerializer(read_only=True)

    class Meta:
        model = Actividad
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    cedula = UsuarioSerializer(read_only=True)  #SERIALIZER_ANIDADO
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Actividad
        fields = '__all__'

