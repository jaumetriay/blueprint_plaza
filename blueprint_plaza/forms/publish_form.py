from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    base_price = FloatField('Base Price', validators=[DataRequired()])
    expected_price = FloatField('Expected Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')