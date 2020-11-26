from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError

from app.model import User


class LoginForm(FlaskForm):
    username = StringField("UserName: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    username = StringField("UserName: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    password2 = PasswordField("Password: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    phone = StringField("Phone: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Этот username занят')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Этот email занят')


