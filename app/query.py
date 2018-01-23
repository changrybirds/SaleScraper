from app import app, db, scraper
from app.models import Tracker
from datetime import datetime
from twilio.rest import Client

account_sid = "placeholder"
auth_token = "placeholder"
client = Client(account_sid, auth_token)

def dbQuery():
	trackers = Tracker.query.all()
	for t in trackers:
		sale_status = scraper.scrape_sale_status(t.vendor, t.url)
		if sale_status:
			print(True) # insert correct text
		else:
			time_diff = datetime.utcnow - t.timestamp
			if time_diff.total_seconds() > 31557600:
				db.session.delete(t)
				db.session.commit()
			else:
				print(False) # insert correct text


def notify(phone, vendor):
	client.api.account.messages.create(
		to=phone, 
		from_="twilio number here", 
		body="Your item from " + vendor + " is on sale!")
