from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash

from app.extensions import login_manager, db
from app.model.user import User
from .forms import LoginForm, RegisterForm

blueprint = Blueprint('route', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('messenger/home.html')


@blueprint.route('/login/', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None:
                password = generate_password_hash(form.password.data)
                if user.check_password(password=password):
                    login_user(user)
                    return redirect('home')
    form = LoginForm()
    return render_template('messenger/login.html', form=form)


@blueprint.route('/register/', methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, phone=form.phone.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Успех')
            login_user(user)
            return redirect('/')
    form = RegisterForm()
    return render_template('messenger/register.html', title='Register', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
