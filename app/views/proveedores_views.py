from flask import Blueprint, render_template

proveedores_views = Blueprint('proveedor', __name__)

@proveedores_views.route('/proveedor/categories/')
def proveedores_categories():
    return render_template('categories/proveedores_categories.html')
