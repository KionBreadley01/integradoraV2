from flask import Blueprint, render_template, redirect, url_for, flash

from models.proveedor import Proveedor

from forms.proveedor_forms import ProveedorCreateForm, ProveedorUpdateForm
proveedores_views = Blueprint('proveedor', __name__)

@proveedores_views.route('/proveedor/categories/')
def proveedores_categories():
    proveedores = Proveedor.get_all()
    return render_template('categories/proveedores_categories.html',
                           proveedores=proveedores)


@proveedores_views.route('/proveedores/create/', methods=('GET', 'POST'))
def create_proveedor():
    form = ProveedorCreateForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        Ape_pat = form.Ape_pat.data
        Ape_mat = form.Ape_mat.data
        Direccion = form.Direccion.data
        id_tela = form.id_tela.data
        proveedor = Proveedor(None, nombre, Ape_pat, Ape_mat, Direccion, id_tela)
        proveedor.save()
        return redirect(url_for('proveedor.create_proveedor'))
    return render_template('categories/create_prov.html', form=form)

@proveedores_views.route('/proveedores/<int:id>/update/', methods=('GET', 'POST'))
def update_proveedor(id):
    form = ProveedorUpdateForm()
    proveedor = Proveedor.get(id)
    if form.validate_on_submit():
        proveedor.nombre = form.nombre.data
        proveedor.Ape_pat = form.Ape_pat.data
        proveedor.Ape_mat = form.Ape_mat.data
        proveedor.Direccion = form.Direccion.data
        proveedor.id_tela = form.id_tela.data
        proveedor.save()
        return redirect(url_for('proveedor.create_proveedor'))
    form.nombre.data = proveedor.nombre
    form.Ape_pat.data = proveedor.Ape_pat
    form.Ape_mat.data = proveedor.Ape_mat
    form.Direccion.data = proveedor.Direccion
    form.id_tela.data = proveedor.id_tela
    return render_template('categories/create_prov.html', form=form)

@proveedores_views.route('/proveedores/<int:id>/delete/', methods=('POST',))
def delete_proveedor(id):
    proveedor = Proveedor.get(id)
    proveedor.delete()
    return redirect(url_for('proveedor.create_proveedor'))
