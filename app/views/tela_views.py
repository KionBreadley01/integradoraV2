from flask import Blueprint, render_template

tela_views = Blueprint('tela', __name__)

@tela_views.route('/tela/', methods=['GET'])
def tela_categories():
    return render_template('categories/tela_categories.html')