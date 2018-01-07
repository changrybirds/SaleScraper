from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length, URL

class TrackingForm(FlaskForm):
	phone_number = IntegerField('10-digit phone number', validators=[
		InputRequired(), Length(10, 15)])

	vendor_list = [
		('br', 'Banana Republic'), ('jc', 'J.Crew'), ('ex', 'Express'), ('ns','Nordstrom')]

	vendor = SelectField('Retailer', choices=vendor_list, validators=[InputRequired()])

	url = StringField('Product URL', validators=[
		InputRequired(), URL(True, 'Please enter a valid URL')])

	submit = SubmitField('Submit')