from app import app, db, scraper
from app.models import Tracker

def dbQuery():
	trackers = Tracker.query.all()
	for t in trackers:
		sale_status = scraper.scrape_sale_status(t.vendor, t.url)
		if sale_status:
			return True # insert correct text
		else:
			return False # insert correct text
