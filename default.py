# -*- coding: utf-8 -*-
import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):

    self.response.out.write("Hello World \o/")

    self.response.set_status(200)

application = webapp2.WSGIApplication([
								('/', MainHandler),
								('/.*', MainHandler)
                              	], debug=True)
