# -*- coding: utf-8 -*-
import webapp2
import datetime
import json
import logging
import calendar

from objects.workingday import working_day
from objects.work import work
from objects.mytime import my_time

from utils.valid_request_util import check
from utils.header_helper import header_helper

from google.appengine.ext import db
from databases import TimeTrackDay
from databases import TimeTrack

class GetHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    if check.token_and_headers(token, self.request.headers):
        year = json_string['year']
        month = json_string['month']
        last_day_in_month = calendar.monthrange(year,month)[1]

        query = 'SELECT * FROM TimeTrackDay WHERE day >= DATE(:1,:2,1) AND day <= DATE(:1,:2,:3) AND token = \'' + token + '\''
        time_track_day_db = db.GqlQuery(query, year, month, last_day_in_month)
        response_working = {}
        response_month = working_day(year, month, None)
        response_working["working_month"] = response_month.__dict__
        response_work_list = []
        for track_day in time_track_day_db:
            response_working_each_day = {}
            response_work_day = working_day(track_day.day.year, track_day.day.month, track_day.day.day)
            response_working_each_day["working_day"] = response_work_day.__dict__
            time_track_db = TimeTrack.all().ancestor(track_day.key()).order('start_time')
            response_work_each_day_list = []
            for track in time_track_db:
                reponse_work_start_time = my_time(track.start_time.hour, track.start_time.minute)
                reponse_work_end_time = my_time(track.end_time.hour, track.end_time.minute)
                response_track = {
                    "name" : track.name,
                    "start_time" : reponse_work_start_time.__dict__,
                    "end_time" : reponse_work_end_time.__dict__,
                    "illness" : track.illness,
                    "vacation" : track.vacation
                }
                response_work_each_day_list.append(response_track)
            response_working_each_day["work_in_day"] = response_work_each_day_list
            response_work_list.append(response_working_each_day)

        response_working["work"] = response_work_list
        logging.info(json.dumps(response_working))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(response_working))
        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/work/get', GetHandler)
                              	], debug=True)
