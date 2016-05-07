# -*- coding: utf-8 -*-
import webapp2
import datetime
import json
import logging

from objects.working import working

from utils.token_helper import token_helper
from utils.header_helper import header_helper

from google.appengine.ext import db
from databases import TimeTrackDay
from databases import TimeTrack

from utils.create_user_utils import user_util

class CreateHandler(webapp2.RequestHandler):
  def post(self):
    body = self.request.body
    json_string = json.loads(body)
    logging.info(json_string)

    h_helper = header_helper(self.request.headers)
    if h_helper.valid_auth() and h_helper.valid_api_version() == "1":
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
    else:
        self.response.set_status(401)

  def get(self):
    self.redirect("/")

application = webapp2.WSGIApplication([
								('/rest/user/create', CreateHandler)
                              	], debug=True)
