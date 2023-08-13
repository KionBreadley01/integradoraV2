# views/maquilero.py
from flask import Blueprint, render_template, redirect, url_for, flash

from models.maquilero import Maquilero

from forms.maquilero_forms import MaquileroCreateForm, MaquileroUpdateForm

maquilero_views = Blueprint('maquilero', __name__)

@maquilero_views.route('/maquileros/')
def maquilero():
    maquileros = Maquilero.get_all() 
    return render_template('categories/maquileros_categories.html',
                            maquileros=maquileros)

@maquilero_views.route('/maquileros/create/', methods=('GET', 'POST'))
def create_maquilero():
    form = MaquileroCreateForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        Ape_pat = form.Ape_pat.data
        Ape_mat = form.Ape_mat.data
        Direccion = form.Direccion.data
        maquilero = Maquilero(None, nombre, Ape_pat, Ape_mat, Direccion)
        maquilero.save()
        return redirect(url_for('maquilero.maquilero'))
    return render_template('categories/create_maq.html', form=form)

@maquilero_views.route('/maquileros/<int:id>/update/', methods=('GET', 'POST'))
def update_maquilero(id):
    form = MaquileroUpdateForm()
    maquilero = Maquilero.get(id)
    if form.validate_on_submit():
        maquilero.nombre = form.nombre.data
        maquilero.Ape_pat = form.Ape_pat.data
        maquilero.Ape_mat = form.Ape_mat.data
        maquilero.Direccion = form.Direccion.data
        maquilero.save()
        return redirect(url_for('maquilero.maquilero'))
    form.nombre.data = maquilero.nombre
    form.Ape_pat.data = maquilero.Ape_pat
    form.Ape_mat.data = maquilero.Ape_mat
    form.Direccion.data = maquilero.Direccion
    return render_template('categories/create_maq.html', form=form)

@maquilero_views.route('/maquileros/<int:id>/delete/', methods=('POST',))
def delete_maquilero(id):
    maquilero = Maquilero.get(id)
    maquilero.delete()
    return redirect(url_for('maquilero.maquilero'))

