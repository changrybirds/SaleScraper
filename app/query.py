from app import app, db, scraper, notify
from app.models import Tracker
from datetime import datetime


def dbQuery():
  trackers = Tracker.query.all()
  for t in trackers:
    vendor = t.vendor
    url = t.url
    phone = t.phone_number

    sale_status = scraper.scrape_sale_status(vendor, url)

    if sale_status:
      notify.notify_sale(phone, vendor, url)

      # delete from database following match
      db.session.delete(t)
      db.session.commit()

    else:
      time_diff = datetime.utcnow - t.timestamp
      if time_diff.total_seconds() > 31557600:
        db.session.delete(t)
        db.session.commit()
      else:
        pass
