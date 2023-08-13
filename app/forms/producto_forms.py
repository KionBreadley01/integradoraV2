from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ProductoCreateForm(FlaskForm):
    nombre_producto = StringField('Nombre del Producto', 
                                  validators=[DataRequired()])
    tipo_tela = StringField('Tipo de Tela',
                            validators=[DataRequired()])
    talla = StringField('Talla', 
                        validators=[DataRequired()])
    submit = SubmitField('Guardar')

class ProductoUpdateForm(FlaskForm):
    nombre_producto = StringField('Nombre del Producto', 
                                  validators=[DataRequired()])
    tipo_tela = StringField('Tipo de Tela',
                            validators=[DataRequired()])
    talla = StringField('Talla', 
                        validators=[DataRequired()])
    submit = SubmitField('Actualizar')
