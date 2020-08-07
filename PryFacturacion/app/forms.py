from app.models import *
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion',
                  'precio',
                  'stock',
                  'iva')
        label = {
            'descripcion': 'Producto',
            'precio': 'Precio',
            'stock': 'Stock',
            'iva':'Iva'}
        widgets={

            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'type':'number',
                    'step':'any',
                    'value':'0',
                    'class': 'form-control'

                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'number',
                    'value':'0',
                    'class': 'form-control'


                }
            ),
            'iva': forms.CheckboxInput(
                attrs={
                    'class': 'field-iva'

                }
            )
        }

#Formulario de Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc',
                  'nombre',
                  'direccion',
                  'producto')
        label = {
            'ruc': 'Ruc',
            'nombre': 'Nombre del Cliente',
            'direccion': 'Dirección'}
        widgets={

            'ruc':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'direccion': forms.Textarea(
                attrs={
                    'class': 'form-control'

                }
            ),
            'producto': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }


#detalle dactura

class detalleForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ('factura',
                  'producto',
                  'cantidad',
                  'precio',
                  'subtotal')
        label = {
                  'factura':'Factura',
                  'producto':'Producto',
                  'cantidad':'Cantidad',
                  'precio':'Precio',
                  'subtotal':'Subtotal'}
        widgets={

            'factura':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'producto': forms.Select(
                attrs={
                    'class': 'form-control'

                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'number',
                    'value':'0',
                    'class': 'form-control'

                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'type': 'number',
                    'step': 'any',
                    'value': '0',
                    'class': 'form-control'

                }
            ),
            'subtotal': forms.TextInput(
                attrs={
                    'type': 'number',
                    'step': 'any',
                    'value': '0',
                    'class': 'form-control'

                }
            )

        }