from flask import Blueprint, render_template, redirect, url_for
from models.tipo_tela import TipoTela
from forms.tipo_tela_forms import CreateTipoTelaForm, UpdateTipoTelaForm

tipo_tela_views = Blueprint('tipo_tela', __name__)

@tipo_tela_views.route('/tipo_telas/')
def tipo_tela():
    tipos_tela = TipoTela.get_all()
    return render_template('categories/tipo_tela.html', 
                           tipos_tela=tipos_tela)

@tipo_tela_views.route('/tipo_telas/create/', methods=('GET', 'POST'))
def create_tipo_tela():
    form = CreateTipoTelaForm()
    if form.validate_on_submit():
        id_tela = form.id_tela.data
        nombre_tela = form.nombre_tela.data
        precio = form.precio.data
        tipo_tela = TipoTela(id_tela, nombre_tela, precio)
        tipo_tela.save()
        return redirect(url_for('tipo_tela.tipo_tela'))
    return render_template('categories/create_tipo_tela.html', form=form)

@tipo_tela_views.route('/tipo_telas/<int:id>/update/', methods=('GET', 'POST'))
def update_tipo_tela(id):
    form = UpdateTipoTelaForm()
    tipo_tela = TipoTela.get(id)
    if form.validate_on_submit():
        tipo_tela.id_tela = form.id_tela.data
        tipo_tela.nombre_tela = form.nombre_tela.data
        tipo_tela.precio = form.precio.data
        tipo_tela.save()
        return redirect(url_for('tipo_tela.tipo_tela'))
    form.id_tela.data = tipo_tela.id_tela
    form.nombre_tela.data = tipo_tela.nombre_tela
    form.precio.data = tipo_tela.precio
    return render_template('categories/create_tipo_tela.html', form=form)

@tipo_tela_views.route('/tipo_telas/<int:id>/delete/', methods=('POST',))
def delete_tipo_tela(id):
    tipo_tela = TipoTela.get(id)
    tipo_tela.delete()
    return redirect(url_for('tipo_tela.tipo_tela'))
