from flask import Blueprint
from flask import render_template,request,flash,redirect, url_for
from flask_login import login_user, logout_user, login_required,current_user
from .models import User
from .forms import LoginForm,registerForm
from . import login_manager
from .queries import queries

page=Blueprint('page',__name__)

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html')

@page.route('/')
def index():
    return redirect(url_for('.login'))

@page.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@page.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.get_by_User_Name(form.User_Name.data)
        if user and user.verify_password(form.Password.data):
            login_user(user)
            return redirect(url_for('.home'))
        flash('Usuario y/o contraseña invalidos','error')

    return render_template('auth/login.html',form=form)

@page.route ('/register', methods=['GET','POST'] )
@login_required
def register():
    form = registerForm(request.form)
    Name = queries.Name_user()
    Account_Type = current_user.Account_Type
    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.Name.data,form.Last_Name.data,form.Account_Type.data,form.User_Name.data,form.Password.data)
            flash('Usuario creado se a registrado exitosamente')
    return render_template('auth/register.html',form=form,Name=Name,Account_Type=Account_Type)

@page.route('/home')
@login_required
def home():
    Name = queries.Name_user()
    Account_Type = current_user.Account_Type
    return render_template('home.html',Name=Name,Account_Type=Account_Type)

@page.route('/list_user')
@login_required
def list_user():
    Name = queries.Name_user()
    Account_Type = current_user.Account_Type
    Users = queries.Users_list()
    return render_template('users/list.html',Name = Name,Account_Type = Account_Type,Users = Users)
