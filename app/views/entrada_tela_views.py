from flask import Blueprint, render_template, redirect, url_for, flash

from models.entrada_tela import EntradaTela
from forms.entrada_tela_forms import EntradaTelaCreateForm, EntradaTelaUpdateForm

entrada_tela_views = Blueprint('entrada_tela', __name__)

@entrada_tela_views.route('/entradas_tela/')
def entrada_tela():
    entradas = EntradaTela.get_all()
    return render_template('categories/tela_categories.html', entradas=entradas)

@entrada_tela_views.route('/entradas_tela/create/', methods=('GET', 'POST'))
def create_entrada_tela():
    form = EntradaTelaCreateForm()
    if form.validate_on_submit():
        id_proveedor = form.id_proveedor.data
        id_tela = form.id_tela.data
        tela = form.Tela.data
        metros = form.Metros.data
        fecha_entrada = form.fecha_entrada.data
        entrada_tela = EntradaTela(None, id_proveedor, id_tela, tela, metros, fecha_entrada)
        entrada_tela.save()
        return redirect(url_for('entrada_tela.entrada_tela'))
    return render_template('categories/create_tela.html', form=form)

@entrada_tela_views.route('/entradas_tela/<int:id>/update/', methods=('GET', 'POST'))
def update_entrada_tela(id):
    form = EntradaTelaUpdateForm()
    entrada_tela = EntradaTela.get(id)
    if form.validate_on_submit():
        entrada_tela.id_proveedor = form.id_proveedor.data
        entrada_tela.id_tela = form.id_tela.data
        entrada_tela.tela = form.Tela.data
        entrada_tela.metros = form.Metros.data
        entrada_tela.fecha_entrada = form.fecha_entrada.data
        entrada_tela.save()
        return redirect(url_for('entrada_tela.entrada_tela'))
    form.id_proveedor.data = entrada_tela.id_proveedor
    form.id_tela.data = entrada_tela.id_tela
    form.Tela.data = entrada_tela.tela
    form.Metros.data = entrada_tela.metros
    form.fecha_entrada.data = entrada_tela.fecha_entrada
    return render_template('categories/create_tela.html', form=form)

@entrada_tela_views.route('/entradas_tela/<int:id>/delete/', methods=('POST',))
def delete_entrada_tela(id):
    entrada_tela = EntradaTela.get(id)
    entrada_tela.delete()
    return redirect(url_for('entrada_tela.entrada_tela'))