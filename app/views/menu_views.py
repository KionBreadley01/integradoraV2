from flask import Blueprint, render_template

menu_views = Blueprint('menu', __name__)

@menu_views.route('/menu_categories/')
def menu_categories():
    return render_template('categories/menu_categories.html')



