# -*- coding: utf-8 -*-
import webapp2
import datetime
import json
import logging

from objects.working import working

from tokenhelper import token_helper
from header_helper import header_helper

from google.appengine.ext import db
from databases import TimeTrackDay
from databases import TimeTrack

class SaveHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)
    work = working.create_from_json(json_string)

    t_helper = token_helper(work.token)
    h_helper = header_helper(self.request.headers)
    if t_helper.valid_token and h_helper.valid_auth() and h_helper.valid_api_version() == "1":
        self.save_time_track(work)
        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def save_time_track(self, working):
    query = TimeTrackDay.all()
    query = query.filter('day =',  datetime.datetime(working.working_day.year, working.working_day.month, working.working_day.day))
    result = query.get()
    if result is None:
        self.save_time_tracks_in_db(working, TimeTrackDay())
    else:
        self.delete_old_time_tracks(result.key())
        self.save_time_tracks_in_db(working, TimeTrackDay(key=result.key()))

  def delete_old_time_tracks(self, key):
    time_track_db = TimeTrack.all()
    time_track_db = time_track_db.ancestor(key)
    for time_track in time_track_db:
      time_track.delete()

  def save_time_tracks_in_db(self, working, time_track_day_db):
    time_track_day_db.token = working.token
    time_track_day_db.day = datetime.date(year=working.working_day.year, month=working.working_day.month, day=working.working_day.day)
    time_track_day_db.put()
    for index in range(0, len(working.work_list)):
        work = working.work_list[index]

        time_track_db = TimeTrack(parent=time_track_day_db)
        time_track_db.name = work.name
        time_track_db.start_time = datetime.time(hour=work.start_time.hour, minute=work.start_time.minute)
        time_track_db.end_time = datetime.time(hour=work.end_time.hour, minute=work.end_time.minute)
        time_track_db.break_time = work.break_time
        time_track_db.put()

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/save', SaveHandler)
                              	], debug=True)
