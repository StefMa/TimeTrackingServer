# -*- coding: utf-8 -*-
import webapp2
import json
import logging

from tokenhelper import token_helper
from header_helper import header_helper

from google.appengine.ext import db
from databases import Settings

class UpdateSettingsHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    token = json_string["token"]
    t_helper = token_helper(token)
    h_helper = header_helper(self.request.headers)
    if t_helper.valid_token and h_helper.valid_auth() and h_helper.valid_api_version() == "1":
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
    t_helper = token_helper(token)
    h_helper = header_helper(self.request.headers)
    if t_helper.valid_token and h_helper.valid_auth() and h_helper.valid_api_version() == "1":
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
								('/rest/settings/update', UpdateSettingsHandler),
                                ('/rest/settings/get', GetSettingsHandler),
                              	], debug=True)
