from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired


class HomeForm(FlaskForm):
    # email = EmailField('Почта', validators=[DataRequired()])
    # password = PasswordField('Пароль', validators=[DataRequired()])
    # remember_me = BooleanField('Запомнить меня')
    # submit = SubmitField('Войти')
    status = SubmitField("Заказ", validators=[DataRequired()])
    pass
