# -*- coding: utf-8 -*-
import webapp2
import logging
import jinja2
import os
import binascii

from google.appengine.ext import db
from databases import User

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

    user = db.GqlQuery("SELECT * FROM User where username = '" + username + "'").get()
    if user is None:
      token = binascii.hexlify(os.urandom(18))

      user_db = User()
      user_db.username = username
      user_db.token = token
      user_db.put()

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
