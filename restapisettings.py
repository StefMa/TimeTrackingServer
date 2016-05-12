# -*- coding: utf-8 -*-
import webapp2
import json
import logging

from utils.valid_request_util import check

from google.appengine.ext import db
from databases import Settings

class UpdateSettingsHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    if check.token_and_headers(token, self.request.headers):
        default_worktime = json_string["settings"]["default_worktime"]

        settings_db = Settings.all().filter("token =", token)
        setting = settings_db.get()
        if setting == None:
            settings_db = Settings()
            settings_db.token = token
            settings_db.default_worktime = default_worktime
            settings_db.put()
        else:
            setting.default_worktime = default_worktime
            setting.put()
        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

class GetSettingsHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    if check.token_and_headers(token, self.request.headers):
        settings_db = Settings.all().filter("token =", token)
        setting = settings_db.get()
        result = {}
        if setting != None:
            result = {
                "default_worktime" : setting.default_worktime
            }
        self.response.out.write(json.dumps(result))
        self.response.set_status(200)
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/user/settings/update', UpdateSettingsHandler),
                                ('/rest/user/settings/get', GetSettingsHandler),
                              	], debug=True)
