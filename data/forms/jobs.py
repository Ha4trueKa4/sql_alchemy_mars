from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job_name = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField("Время работы (в часах)")
    team_leader = IntegerField("Идентифифкатор лидера")
    collaborators = StringField('Коллабораторы', validators=[DataRequired()])
    is_finished = BooleanField("Работа завершена")
    submit = SubmitField('Применить')