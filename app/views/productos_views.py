
from flask import Blueprint, render_template

productos_views = Blueprint('productos', __name__)

@productos_views.route('/productos/categories')
def productos_categories():
    return render_template('categories/productos_categories.html')