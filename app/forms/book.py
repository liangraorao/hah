from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):

    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='q的长度要在1-30之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)