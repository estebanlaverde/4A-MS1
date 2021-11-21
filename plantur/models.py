from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40) 

class Ciudades(models.Model):
    nombre = models.CharField(max_length=30)
    clima = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)

class Actividad(models.Model):
    tipo = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.TextField(blank=True)
    ciudad_Act = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)

class Hoteles(models.Model):
    nit_hotel = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=30)
    fechainicio = models.CharField(max_length=20)
    fechafinal = models.CharField(max_length=20)
    tarifa = models.CharField(max_length=20)
    ciudad_hotel = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)

class Proveedor(models.Model):
    nit_proveedor = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion_proveedor = models.CharField(max_length=40)
    telefono = models.CharField(max_length=30)
    actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True)
    ciudad_Prov = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)

class Transporte(models.Model):
    nit_transporte = models.CharField(max_length=30, primary_key=True)
    tipo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    fechainicio = models.CharField(max_length=20)
    fechafinal = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
    ciudad_Transp = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)


class Plan(models.Model):
    valor = models.CharField(max_length=20)
    fechainicio = models.CharField(max_length=20)
    fechafinal = models.CharField(max_length=20)
    tipo_actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True)
    ciudad_Plan = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, null=True)
    cedula = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    nit_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    nit_transporte = models.ForeignKey(Transporte, on_delete=models.SET_NULL, null=True)
    nit_hotel = models.ForeignKey(Hoteles, on_delete=models.SET_NULL, null=True)

class Factura(models.Model):
    cedula = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=50)
    mediopago = models.CharField(max_length=40)
    valor = models.CharField(max_length=20)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)

