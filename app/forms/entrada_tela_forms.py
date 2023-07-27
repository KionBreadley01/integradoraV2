from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired

class CreateEntradaTelaForm(FlaskForm):
    id_proveedor = StringField('ID Proveedor', validators=[DataRequired()])
    id_tela = StringField('ID Tela', validators=[DataRequired()])
    tela = StringField('Tela', validators=[DataRequired()])
    metros = DecimalField('Metros', validators=[DataRequired()])
    fecha_entrada = DateField('Fecha de Entrada', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Guardar')
