# -*- coding: utf-8 -*-
import webapp2
import datetime
import json
import logging
import calendar

from objects.workingday import working_day
from objects.work import work
from objects.mytime import my_time

from tokenhelper import token_helper

from google.appengine.ext import db
from databases import TimeTrackDay
from databases import TimeTrack

class DeleteHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    t_helper = token_helper(token)
    if t_helper.valid_token:
        work_day = working_day(json_string['working_day']['year'], json_string['working_day']['month'], json_string['working_day']['day'])

        query = 'SELECT * FROM TimeTrackDay WHERE day = DATE(:1,:2,:3) AND token = \'' + token + '\''
        time_track_day_db = db.GqlQuery(query, work_day.year, work_day.month, work_day.day)
        track_day = time_track_day_db.get()
        time_track_db = TimeTrack.all()
        time_track_db = time_track_db.ancestor(track_day.key())
        for time_track in time_track_db:
          time_track.delete()
        track_day.delete()
        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/delete', DeleteHandler)
                              	], debug=True)
