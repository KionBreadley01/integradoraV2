from flask import Blueprint, render_template, redirect, url_for, flash

from models.producto import Producto  # Importar el modelo de Producto
from forms.producto_forms import ProductoCreateForm, ProductoUpdateForm  # Importar los formularios

productos_views = Blueprint('productos', __name__)

@productos_views.route('/productos/categories')
def productos_categories():
    productos = Producto.get_all()  # Obtener todos los productos
    return render_template('categories/productos_categories.html', productos=productos)

@productos_views.route('/productos/create/', methods=('GET', 'POST'))
def create_producto():
    form = ProductoCreateForm()
    if form.validate_on_submit():
        nombre_producto = form.nombre_producto.data
        tipo_tela = form.tipo_tela.data
        talla = form.talla.data
        producto = Producto(None, nombre_producto, tipo_tela, talla)
        producto.save()
        return redirect(url_for('productos.productos_categories'))
    return render_template('categories/create_prod.html', form=form)

@productos_views.route('/productos/<int:id>/update/', methods=('GET', 'POST'))
def update_producto(id):
    form = ProductoUpdateForm()
    producto = Producto.get(id)
    if form.validate_on_submit():
        producto.nombre_producto = form.nombre_producto.data
        producto.tipo_tela = form.tipo_tela.data
        producto.talla = form.talla.data
        producto.save()
        return redirect(url_for('productos.productos_categories'))
    form.nombre_producto.data = producto.nombre_producto
    form.tipo_tela.data = producto.tipo_tela
    form.talla.data = producto.talla
    return render_template('categories/create_prod.html', form=form)

@productos_views.route('/productos/<int:id>/delete/', methods=('POST',))
def delete_producto(id):
    producto = Producto.get(id)
    producto.delete()
    return redirect(url_for('productos.productos_categories'))