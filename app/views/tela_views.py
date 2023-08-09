from flask import Blueprint, render_template,redirect, url_for, flash


tela_views = Blueprint('tela', __name__)

@tela_views.route('/tela/', methods=['GET'])
def tela_categories():
    
    return render_template('categories/tela_categories.html')




