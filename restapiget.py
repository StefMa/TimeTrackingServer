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
        response = None
        if time_track_db.count() >= 1:
            response = '{ "working_month" : { "year" : ' + str(year) + ', "month" : ' + str(month) + ' }, work ['
        for track in time_track_db:
            response += '{'
            response += '"working_day" : { "year" : ' + str(track.day.year) + ', "month" : ' + str(track.day.month) + ', "day" : ' + str(track.day.day) + ' },'
            response += '"start_time" : { "hour" : ' + str(track.start_time.hour) + ', "minute" : ' + str(track.start_time.minute) + ' },'
            response += '"end_time" : { "hour" : ' + str(track.end_time.hour) + ', "minute" : ' + str(track.end_time.minute) + ' },'
            response += '"break_time" : ' + str(track.break_time)
            response += '},'

        if response is not None:
            response = response[:-1]
            response += '] }'
            logging.info(json.dumps(response))
            self.response.out.write(json.dumps(response))
            self.response.set_status(200)
        else:
            self.response.set_status(404)
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/get', GetHandler)
                              	], debug=True)
