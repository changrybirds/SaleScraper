from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TrackingForm

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
	form = TrackingForm()
	if form.validate_on_submit():
		return redirect('success')
	return render_template('index.html', form=form)

@app.route('/success')
def success():
	return render_template('success.html')