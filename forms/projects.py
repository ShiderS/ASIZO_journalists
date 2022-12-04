from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class ProjectsForm(FlaskForm):
    # title = StringField('Название', validators=[DataRequired()])
    # content = TextAreaField("Содержание")
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    middle_name = StringField('Отчество', validators=[DataRequired()])
    post = StringField('Должность', validators=[DataRequired()])
    place = StringField('Место работы', validators=[DataRequired()])
    topic = StringField('Тема работы', validators=[DataRequired()])
    heading = StringField('Заголовок работы', validators=[DataRequired()])
    annotation = TextAreaField('Аннотация', validators=[DataRequired()])
    # is_private = BooleanField("Личное")
    image = FileField('Изображение')
    submit = SubmitField('Применить')
