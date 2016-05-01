# -*- coding: utf-8 -*-
from google.appengine.ext import db
from databases import User

import os
import binascii

# Create a user with username in DB.
# Return token if successfull. Or None otherwise
class user_util():
    @staticmethod
    def create_user(username):
        user = db.GqlQuery("SELECT * FROM User where username = '" + username + "'").get()
        if user is None:
          token = binascii.hexlify(os.urandom(18))

          user_db = User()
          user_db.username = username
          user_db.token = token
          user_db.put()

          return token
        return None
