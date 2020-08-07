"""PryFacturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menu,name='index'),
    path('producto/',read_Producto,name='view_producto'),
    path('nuevoProducto/',create_Producto,name='create_producto'),
    path('editarProducto/<int:id>',edit_Producto,name='edit_producto'),
    path('eliminarProducto/<int:id>',delete_Producto,name='delete_producto'),
    #url cliente
    path('cliente/',read_Cliente,name='view_cliente'),
    path('nuevoCliente/',create_Cliente,name='create_cliente'),
    path('editarCliente/<int:id>',edit_Cliente,name='edit_cliente'),
    path('eliminarCliente/<int:id>',delete_Cliente,name='delete_cliente'),
    #url venta-factura
    path('venta/',read_Venta,name='view_venta'),
    #url detalleFactura
    path('detalleFactura/',read_detalle,name='view_detalleFactura'),
    path('nuevoDetalleFactura/',create_detalle,name='create_detalleFactura'),
    path('editarDetalleFactura/<int:id>',edit_detalleFactura,name='edit_detalleFactura'),
    path('eliminarDetalleFactura/<int:id>',delete_detalle,name='delete_detalleFactura'),
]
