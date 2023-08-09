from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MaquileroCreateForm(FlaskForm):
    nombre = StringField('nombre', 
                         validators=[DataRequired()])
    Ape_pat = StringField('Apellido Paterno',
                           validators=[DataRequired()])
    Ape_mat = StringField('Apellido Materno', 
                          validators=[DataRequired()])
    Direccion = StringField('Dirección',
                             validators=[DataRequired()])
    submit = SubmitField('Guardar')

class MaquileroUpdateForm(FlaskForm):
    nombre = StringField('nombre', 
                         validators=[DataRequired()])
    Ape_pat = StringField('Apellido Paterno',
                           validators=[DataRequired()])
    Ape_mat = StringField('Apellido Materno', 
                          validators=[DataRequired()])
    Direccion = StringField('Dirección',
                             validators=[DataRequired()])
    submit = SubmitField('Actualizar')
