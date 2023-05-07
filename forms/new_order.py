from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, FloatField, TimeField
from wtforms.validators import DataRequired, ValidationError

from data.help_functions import check_address
from data.variables import regions_table


def validate_region(form, field):
    if field.data not in regions_table.keys():
        raise ValidationError("Регион должен существовать в РФ")


def validate_weight(form, field):
    if not (0.1 <= field.data <= 50):
        raise ValidationError("Вес должен лежать в пределах от 0.1 до 50")


def validate_address(form, field):
    if not check_address(field.data):
        raise ValidationError("Адрес некорректен")


class MakeOrderForm(FlaskForm):
    weight = FloatField('Вес заказа (в кг)', validators=[DataRequired("Неверный формат веса"), validate_weight])
    region = IntegerField('Регион заказа',
                          validators=[DataRequired(message="Неверный формат региона"), validate_region])
    address = StringField('Адрес (достаточно улицы)',
                          validators=[DataRequired(message="Введите адрес"), validate_address])
    workhours_start = TimeField("Время доставки с",
                                validators=[DataRequired(message="Неверный формат времени начала")])
    workhours_end = TimeField("Время доставки до",
                              validators=[DataRequired(message="Неверный формат времени конца")])
    submit = SubmitField('Сделать заказ')
