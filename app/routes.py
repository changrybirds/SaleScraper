from flask import render_template, flash, redirect, url_for, g
from app import app, db
from app.forms import TrackingForm
from app.models import Tracker



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
  form = TrackingForm()
  if form.validate_on_submit():
    t = Tracker(phone_number=form.phone_number.data, vendor=form.vendor.data, url=form.url.data)
    db.session.add(t)
    db.session.commit()
    return redirect('success')
  else:
    return render_template('index.html', form=form)

@app.route('/success')
def success():
  return render_template('success.html')