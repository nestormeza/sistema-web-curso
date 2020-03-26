from wtforms import Form
from wtforms import validators
from wtforms import StringField,PasswordField,SelectField,HiddenField

from .models import User

class LoginForm(Form):
    User_Name = StringField('Usuario',[
        validators.required()
    ])
    Password = PasswordField('Contraseña',[
        validators.required()
    ])

class registerForm(Form):
    Name = StringField('Nombre',[
        validators.required()
    ])
    Last_Name = StringField('Apellidos',[
        validators.required()
    ])
    Account_Type = SelectField('Tipo de Acceso',
        choices=[('Administrador','Administrador'),('Usuario','Usuario')]
    )
    User_Name = StringField('Usuario',[
        validators.required(),
    ])
    Password = PasswordField('Contraseña',[
        validators.required(),
    ])

    def validate_User_Name(self,User_Name):
        if User.get_by_User_Name(User_Name.data):
            raise validators.ValidationError('El usuario ya se encuentra registrado')
