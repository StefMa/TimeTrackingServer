# -*- coding: utf-8 -*-
from google.appengine.ext import db

class token_helper():
    def __init__(self, token):
        self.valid_token = False

        query = "SELECT * FROM User WHERE token = :1"
        valid_user = db.GqlQuery(query, token).get()
        if valid_user is not None:
            self.valid_token = True
