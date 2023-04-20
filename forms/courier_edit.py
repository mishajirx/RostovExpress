from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class EditInfoForm(FlaskForm):
    courier_type = TextAreaField("Мой тип")
    regions = TextAreaField("Мои регионы")
    working_hours = TextAreaField("Мои рабочие часы")
    submit = SubmitField('Изменить')
