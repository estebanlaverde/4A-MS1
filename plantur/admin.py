from django.contrib import admin
from .models import Usuario, Hoteles, Proveedor, Ciudades, Transporte, Actividad, Factura, Plan

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ciudades)
admin.site.register(Actividad)
admin.site.register(Hoteles)
admin.site.register(Proveedor)
admin.site.register(Transporte)
admin.site.register(Plan)
admin.site.register(Factura)
