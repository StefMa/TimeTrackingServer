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

from create_user_utils import user_util

class CreateHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    username = json_string["username"]
    token = user_util.create_user(username)
    if token is not None:
        result = {
            "username" : username,
            "result" : "Ok",
            "token" : token
        }
    else:
        result = {
            "username" : username,
            "result": "Already exist",
            "token" : None
        }
    self.response.out.write(json.dumps(result))
    self.response.set_status(200)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/user/create', CreateHandler)
                              	], debug=True)
