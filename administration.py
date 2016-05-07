# -*- coding: utf-8 -*-
import webapp2
import logging
import jinja2
import os

from google.appengine.ext import db
from databases import User

from utils.create_user_utils import user_util

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AdminHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('/templates/administration.html')
    self.response.out.write(template.render())

    self.response.set_status(200)

  def post(self):
    username = self.request.get("username")
    token = user_util.create_user(username)

    if token is not None:
      template_values = {
        'name' : username,
        'token' : token
      }

      template = JINJA_ENVIRONMENT.get_template('/templates/administration_successful.html')
      self.response.out.write(template.render(template_values))

    else:
      template_values = {
        'error_message' : 'Something is getting wrong'
      }

      template = JINJA_ENVIRONMENT.get_template('/templates/administration_error.html')
      self.response.out.write(template.render(template_values))

    self.response.set_status(200)

application = webapp2.WSGIApplication([
								('/admin', AdminHandler)
                              	], debug=True)
