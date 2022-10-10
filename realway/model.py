from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired

class ExampleForm(FlaskForm):
    date = DateField(label=('Select Date'), format='%Y-%m-%d', validators=[DataRequired()])
    start_s = StringField(label=('Enter Start Station'), validators=[DataRequired()])
    end_s = StringField(label=('Enter End Station'), validators=[DataRequired()])
    submit = SubmitField(label=('Submit'))
