from .models import Category, Classification, Product
from django.forms import ModelForm
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

# Formulario que nos permitira crear categorias de producto
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Destino ',
        }       

# este modelo es para poder editar una categoria
class UpdateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields =  ('name',)
        labels = {
            'name': 'Destino ',
        } 

# Formulario que nos permitira crear tipos de producto
class CreateClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = ('name',)
        labels = {
            'name': 'Tipo Producto ',
        }       

# este modelo es para poder editar una categoria
class UpdateClassificationForm(ModelForm):
    class Meta:
        model = Classification
        fields =  ('name',)
        labels = {
            'name': 'Tipo Producto ',
        } 

# este modelo es para la creacion de productos
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'category', 'classification', 'image')
        labels = {
            'title': 'Producto ',
            'content': 'Detalle ',
            'category': 'Destino ',
            'classification': 'Tipo ',
            'image': 'Imagen ',
        }       

# este modelo es para poder editar un productos
class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  ('title', 'content', 'category', 'classification', 'image')
        labels = {
            'title': 'Producto ',
            'content': 'Detalle ',
            'category': 'Dstino ',
            'classification': 'Tipo ',
            'image': 'Imagen ',
        } 

