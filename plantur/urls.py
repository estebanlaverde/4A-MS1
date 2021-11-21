from django.urls import path 
from .views import UsuarioListCreate, UsuarioUpdateDelete, CiudadesListCreate, CiudadesUpdateDelete, ActividadListCreate,ActividadUpdateDelete, HotelesListCreate, HotelesUpdateDelete, ProveedorListCreate, ProveedorUpdateDelete, TransporteListCreate, TransporteUpdateDelete, PlanListCreate, PlanUpdateDelete, FacturaListCreate, FacturaUpdateDelete

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view()),
    path('usuarios/<pk>/', UsuarioUpdateDelete.as_view()),
    path('ciudades/', CiudadesListCreate.as_view()),
    path('ciudades/<pk>/', CiudadesUpdateDelete.as_view()),
    path('actividades/', ActividadListCreate.as_view()),
    path('actividades/<pk>/', ActividadUpdateDelete.as_view()),
    path('hoteles/', HotelesListCreate.as_view()),
    path('hoteles/<pk>/', HotelesUpdateDelete.as_view()),
    path('proveedores/', ProveedorListCreate.as_view()),
    path('proveedores/<pk>/', ProveedorUpdateDelete.as_view()),
    path('transportes/', TransporteListCreate.as_view()),
    path('transportes/<pk>/', TransporteUpdateDelete.as_view()),
    path('planes/', PlanListCreate.as_view()),
    path('planes/<pk>/', PlanUpdateDelete.as_view()),
    path('facturas/', FacturaListCreate.as_view()),
    path('facturas/<pk>/', FacturaUpdateDelete.as_view())
]