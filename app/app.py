from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Importar Views
from views.home_views import home_views
from views.user_views import user_views
from views.category_views import category_views
from views.error_views import error_views
from views.menu_views import menu_views  # Importamos el Blueprint que contiene la vista del menú
from views.tela_views import tela_views  # Importamos el Blueprint de tela






app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

# Rutas y vistas para el login y registro
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Aquí puedes agregar la lógica para verificar las credenciales del usuario
        # y realizar el inicio de sesión, por ejemplo, usando una base de datos
        return redirect(url_for('home.home'))  # Redireccionar al usuario a la página de inicio
    return render_template('login.html', form=form)

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Aquí puedes agregar la lógica para registrar al usuario en la base de datos
        return redirect(url_for('login'))  # Redireccionar al usuario a la página de inicio de sesión
    return render_template('register.html', form=form)

@app.route('/logout', methods=['POST'])
def logout():
    # Aquí puedes agregar la lógica para cerrar la sesión del usuario
    # Por ejemplo, podrías eliminar la información de la sesión o la cookie de autenticación.
    flash('Logout successful', 'success')  # Muestra un mensaje de éxito cuando el usuario cierra sesión
    return redirect(url_for('home.home'))  # Redirecciona al usuario a la página de inicio


# Registrar Views
app.register_blueprint(home_views)
app.register_blueprint(category_views)
app.register_blueprint(user_views)
app.register_blueprint(error_views)
app.register_blueprint(menu_views)
app.register_blueprint(tela_views)  # Registramos el Blueprint de tela







if __name__ == '__main__':
    app.run(debug=True)
