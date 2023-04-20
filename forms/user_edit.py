from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, RadioField, BooleanField, SelectField, \
    validators
from wtforms.fields import EmailField, IntegerField, TimeField
from wtforms.validators import DataRequired


class EditAboutForm(FlaskForm):
    is_courier = BooleanField("Соглашаюсь с условиями работы")

    type_of_courier = SelectField("Тип курьера",
                                  choices=[('foot', "Пешеход"), ('bike', "Велосипедист"), ('car', "На машинe")])
    region = IntegerField("Ваш регион(номер)", validators=[validators.DataRequired(message="Неверный формат региона")])
    workhours_start = TimeField("Начало рабочего дня",
                                validators=[validators.DataRequired(message="Неверный формат времени начала")])
    workhours_end = TimeField("Конец рабочего дня",
                              validators=[validators.DataRequired(message="Неверный формат времени конца")])

    submit = SubmitField('Подать заявку')
