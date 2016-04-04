# -*- coding: utf-8 -*-
import webapp2
import datetime
import json
import logging

from objects.working import working

from tokenhelper import token_helper

from google.appengine.ext import db
from databases import TimeTrack

class SaveHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)
    work = working.create_from_json(json_string)

    t_helper = token_helper(work.token)
    if t_helper.valid_token:
        self.save_time_track(work.token, work, work.first_work)
        if work.double_working:
          self.save_time_track(work.token, work, work.second_work)

        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def save_time_track(self, token, working, work):
    time_track_db = TimeTrack()
    time_track_db.token = token
    time_track_db.day = datetime.date(year=working.working_day.year, month=working.working_day.month, day=working.working_day.day)
    time_track_db.start_time = datetime.time(hour=work.start_time.hour, minute=work.start_time.minute)
    time_track_db.end_time = datetime.time(hour=work.end_time.hour, minute=work.end_time.minute)
    time_track_db.break_time = work.break_time
    time_track_db.put()

application = webapp2.WSGIApplication([
								('/rest/save', SaveHandler)
                              	], debug=True)
