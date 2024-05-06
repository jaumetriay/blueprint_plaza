from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    base_price = FloatField('Base Price (e.g., 1234.56)', validators=[DataRequired()])
    expected_price = FloatField('Expected Price (e.g., 1234.56)', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')