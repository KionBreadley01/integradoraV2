# tipo_tela_views.py

from flask import Blueprint, render_template

tipo_tela_views = Blueprint('tipo_tela', __name__)

@tipo_tela_views.route('/tipo_tela/', methods=['GET'])
def tipo_tela():
    return render_template('categories/tipo_tela.html')

