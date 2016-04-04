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
from databases import TimeTrack

class GetHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    t_helper = token_helper(token)
    if t_helper.valid_token:
        year = json_string['year']
        month = json_string['month']
        last_day_in_month = calendar.monthrange(year,month)[1]

        query = 'SELECT * FROM TimeTrack WHERE day >= DATE(:1,:2,1) AND day <= DATE(:1,:2,:3) AND token = \'' + token + '\''
        logging.info(query)
        time_track_db = db.GqlQuery(query, year, month, last_day_in_month)
        for track in time_track_db:
            logging.info(str(track.day))
            self.response.out.write(str(track.day) + "<hr>")

        self.response.set_status(200)
    else:
        self.response.set_status(401)

application = webapp2.WSGIApplication([
								('/rest/get', GetHandler)
                              	], debug=True)
