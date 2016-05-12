# -*- coding: utf-8 -*-
from token_helper import token_helper
from header_helper import header_helper

class check():
    @staticmethod
    def token_and_headers(token, headers):
        t_helper = token_helper(token)
        h_helper = header_helper(headers)
        if t_helper.valid_token and h_helper.valid_auth() and h_helper.valid_api_version() == "1":
            return True
        return False
