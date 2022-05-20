from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

from wtforms.validators import InputRequired, NumberRange


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1878, max=2022, message="Enter YYYY"),
        ]
    )

    submit = SubmitField("Add Movie")
