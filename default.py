# -*- coding: utf-8 -*-
import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):

    self.redirect("http://stefma.github.io/TimeTracking/")

application = webapp2.WSGIApplication([
								('/', MainHandler),
								('/.*', MainHandler)
                              	], debug=True)
