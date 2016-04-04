# -*- coding: utf-8 -*-
import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):

    self.response.out.write("Hello World \o/")

application = webapp2.WSGIApplication([
								('/', MainHandler),
								('/.*', MainHandler)
                              	], debug=True)
