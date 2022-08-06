"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Image URL", validators=[Optional()])
    age = RadioField(
        "Age",
        choices=[
            ("baby", "Baby"),
            ("young", "Young"),
            ("adult", "Adult"),
            ("senior", "Senior")
            ],
        validators=[InputRequired(), AnyOf(["baby", "young", "adult", "senior"])]
    )
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Availability", validators=[Optional()])




