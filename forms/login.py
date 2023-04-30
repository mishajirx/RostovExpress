from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired
from wtforms_alchemy import PhoneNumberField


class LoginForm(FlaskForm):
    phone_number = PhoneNumberField("Телефон в формате +7 XXX XXX XX XX", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
