from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

class EntradaTelaCreateForm(FlaskForm):
    id_proveedor = IntegerField('ID Proveedor', 
                                validators=[DataRequired()])
    id_tela = IntegerField('ID Tela', 
                           validators=[DataRequired()])
 
    Tela = StringField('Tela',
                        validators=[DataRequired()])
    Metros = IntegerField('Metros', 
                          validators=[DataRequired()])
    fecha_entrada = DateField('Fecha de Entrada',
                               validators=[DataRequired()])

    submit = SubmitField('Guardar')

class EntradaTelaUpdateForm(FlaskForm):
    id_proveedor = IntegerField('ID Proveedor',
                                 validators=[DataRequired()])
    id_tela = IntegerField('ID Tela', 
                           validators=[DataRequired()])
   
    Tela = StringField('Tela',
                        validators=[DataRequired()])
    Metros = IntegerField('Metros',
                           validators=[DataRequired()])
    fecha_entrada = DateField('Fecha de Entrada', 
                              validators=[DataRequired()])
    submit = SubmitField('Actualizar')
