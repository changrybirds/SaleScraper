from app import db
from datetime import datetime

class Tracker(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	phone_number = db.Column(db.String(24), index=True)
	vendor = db.Column(db.String(64), index=True)
	url = db.Column(db.String(512))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		output = format(self.id) + format(self.phone_number) + format(self.vendor) + format(self.url) + format(self.timestamp)
		return output
