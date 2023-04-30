from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, FloatField, TimeField
from wtforms.validators import DataRequired


class MakeOrderForm(FlaskForm):
    weight = FloatField('Вес заказа', validators=[DataRequired("Неверный формат веса")])
    region = IntegerField('Регион заказа', validators=[DataRequired(message="Неверный формат региона")])
    address = StringField('Адрес (достаточно улицы)', validators=[DataRequired(message="Введите адрес")])
    workhours_start = TimeField("Время доставки с",
                                validators=[DataRequired(message="Неверный формат времени начала")])
    workhours_end = TimeField("Время доставки до",
                              validators=[DataRequired(message="Неверный формат времени конца")])
    submit = SubmitField('Сделать заказ')
