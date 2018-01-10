from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, URL, Regexp
import re

class TrackingForm(FlaskForm):
	phone_regex = re.compile('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')

	phone_number = StringField('10-digit phone number', validators=[
		InputRequired(), Regexp(phone_regex, 0, 'Please enter a 10-digit US phone number')])

	vendor_list = [
		('Banana Republic', 'Banana Republic'), ('J.Crew', 'J.Crew'), ('Express', 'Express'), ('Nordstrom','Nordstrom')]

	vendor = SelectField('Retailer', choices=vendor_list, validators=[InputRequired()])

	url = StringField('Product URL', validators=[
		InputRequired(), URL(True, 'Please enter a valid URL')])

	submit = SubmitField('Submit')

