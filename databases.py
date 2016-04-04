from google.appengine.ext import db

class TimeTrack(db.Model):
  day = db.DateProperty()
  start_time = db.TimeProperty()
  end_time = db.TimeProperty()
  break_time = db.BooleanProperty()
  token = db.StringProperty()

class User(db.Model):
  username = db.StringProperty()
  token = db.StringProperty()
