from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, SelectField, BooleanField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    is_courier = BooleanField("Хочу быть курьером")
    s = "(Для курьеров: <тип>;<регион1>,<регион2>,...;<РабочиеЧасы1(HH:MM-HH:MM)>,<РабочиеЧасы2>,..."
    about = TextAreaField("Немного о себе " + s)
    submit = SubmitField('Войти')
