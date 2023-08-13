# forms/tipo_tela_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, HiddenField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class CreateTipoTelaForm(FlaskForm):
    id_tela = IntegerField('ID Tela', 
                           validators=[DataRequired()])
    nombre_tela = StringField('Nombre de Tela', 
                              validators=[DataRequired()])
    precio = DecimalField('Precio', 
                          validators=[DataRequired()])
    submit = SubmitField('Guardar')

class UpdateTipoTelaForm(FlaskForm):
    id_tela = IntegerField('ID Tela', 
                           validators=[DataRequired()])
    nombre_tela = StringField('Nombre de Tela',
                               validators=[DataRequired()])
    precio = DecimalField('Precio',
                           validators=[DataRequired()])
    submit = SubmitField('Actualizar')
