from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import ProductoForm, ClienteForm, detalleForm
from app.models import Producto, Cliente, Factura, DetalleFactura


def menu(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador'}

    return render(request, 'principal.html', opciones)

#FUNCIONES PRODUCTO

def create_Producto(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'accion':'Crear'}
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_producto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'create_producto.html', opciones)


def read_Producto(request):
    producto = Producto.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'listarProducto': producto}
    return render(request, 'view_producto.html', opciones)



def delete_Producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('view_producto')
    return render(request, 'delete_producto.html', {'producto': producto})


def edit_Producto(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'Administrador': 'Administrador', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('view_producto')

    return render(request, 'create_producto.html', opciones)


#FUNCIONES PARA CLIENTE
def create_Cliente(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas','administrador': 'Administrador', 'accion':'Crear'}
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_cliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'create_cliente.html', opciones)


def read_Cliente(request):
    cliente = Cliente.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'listarCliente': cliente}
    return render(request, 'view_cliente.html', opciones)



def delete_Cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('view_cliente')
    return render(request, 'delete_cliente.html', {'cliente': cliente})


def edit_Cliente(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'Administrador': 'Administrador', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form =ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('view_cliente')

    return render(request, 'create_cliente.html', opciones)



def read_Venta(request):
    venta = Factura.objects.all()
    acumulador= Factura.objects.aggregate(Sum('total'))
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'listarVenta': venta,'totalVenta':acumulador}
    return render(request, 'view_venta.html', opciones)

#Funciones para detalle factura


def create_detalle(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas','administrador': 'Administrador', 'accion':'Crear'}
    if request.method == 'POST':
        # pass
        form = detalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_detalleFactura')
    else:
        form = detalleForm()
        opciones['form'] = form

    return render(request, 'create_detalleFactura.html', opciones)


def read_detalle(request):
    detalle = DetalleFactura.objects.all()
    acumulador = DetalleFactura.objects.aggregate(Sum('subtotal'))
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'listarDetalle': detalle, 'sub':acumulador}
    return render(request, 'view_detalleFactura.html', opciones)



def delete_detalle(request, id):
    detalle = DetalleFactura.objects.get(id=id)
    if request.method == 'POST':
        detalle.delete()
        return redirect('view_detalleFactura')
    return render(request, 'delete_detalleFactura.html', {'detalle': detalle})


def edit_detalleFactura(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'Administrador': 'Administrador', 'accion': 'Actualizar'}
    detalle = DetalleFactura.objects.get(id=id)
    if request.method == 'GET':
        form = detalleForm(instance=detalle)
        opciones['form'] = form
    else:
        form =detalleForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('view_detalleFactura')

    return render(request, 'create_detalleFactura.html', opciones)


#Venta
def read_Venta(request):
    venta = Factura.objects.all()
    acumulador= Factura.objects.aggregate(Sum('total'))
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes','detalleFactura':'Detalle Facturas', 'administrador': 'Administrador', 'listarVenta': venta,'totalVenta':acumulador}
    return render(request, 'view_venta.html', opciones)
