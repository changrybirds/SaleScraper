from flask import render_template
from app import app
from app.forms import TrackingForm

@app.route('/')
@app.route('/index')
def index():
	form = TrackingForm()
	return render_template('index.html', form=form)