from app import db

class Tracker(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	phone_number = db.Column(db.String(24), index=True)
	vendor = db.Column(db.String(64), index=True)
	url = db.Column(db.String(512))

	def __repr__(self):
		return '<Tracker # {}>'.format(self.id)
