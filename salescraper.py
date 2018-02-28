from app import app, db
from app.models import Tracker

# save time importing database instance and models to shell sessions
@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'Tracker': tracker_records}