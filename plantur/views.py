from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer, HotelesSerializer, ProveedorSerializer, CiudadesSerializer, TransporteSerializer, ActividadSerializer, FacturaSerializer, PlanSerializer
from .models import Usuario, Hoteles, Proveedor, Ciudades, Transporte, Actividad, Factura, Plan


# Create your views here.

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CiudadesListCreate(generics.ListCreateAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer

class CiudadesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer

class ActividadListCreate(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class ActividadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class HotelesListCreate(generics.ListCreateAPIView):
    queryset = Hoteles.objects.all()
    serializer_class = HotelesSerializer

class HotelesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hoteles.objects.all()
    serializer_class = HotelesSerializer

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class TransporteListCreate(generics.ListCreateAPIView):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer

class TransporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer

class PlanListCreate(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer 

class PlanUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class FacturaListCreate(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

