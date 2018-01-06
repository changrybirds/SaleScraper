from flast_wtf import FlaskForm
from wtforms import StringField, IntegerField

class TrackingForm(FlaskForm):
	phone_number = IntegerField('10-digit phone number', validators=[
		InputRequired(), Length(10, 15)])
	url = StringField('Product URL', validators=[
		InputRequired(), URL(True, 'Please enter a valid URL')])