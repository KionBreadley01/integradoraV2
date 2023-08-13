from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProveedorCreateForm(FlaskForm):
    nombre = StringField('Nombre', 
                         validators=[DataRequired()])
    Ape_pat = StringField('Apellido Paterno',
                           validators=[DataRequired()])
    Ape_mat = StringField('Apellido Materno', 
                          validators=[DataRequired()])
    Direccion = StringField('Dirección',
                             validators=[DataRequired()])
    id_tela = StringField('ID Tela',
                          validators=[DataRequired()])
    submit = SubmitField('Guardar')

class ProveedorUpdateForm(FlaskForm):
    nombre = StringField('Nombre', 
                         validators=[DataRequired()])
    Ape_pat = StringField('Apellido Paterno',
                           validators=[DataRequired()])
    Ape_mat = StringField('Apellido Materno', 
                          validators=[DataRequired()])
    Direccion = StringField('Dirección',
                             validators=[DataRequired()])
    id_tela = StringField('ID Tela',
                          validators=[DataRequired()])
    submit = SubmitField('Actualizar')
