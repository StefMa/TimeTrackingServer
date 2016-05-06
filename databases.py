from google.appengine.ext import db

class TimeTrackDay(db.Model):
  token = db.StringProperty()
  day = db.DateProperty()
  
class TimeTrack(db.Model):
  name = db.StringProperty()
  start_time = db.TimeProperty()
  end_time = db.TimeProperty()
  break_time = db.BooleanProperty()

class User(db.Model):
  username = db.StringProperty()
  token = db.StringProperty()

class Settings(db.Model):
  token = db.StringProperty()
  default_worktime = db.FloatProperty()
