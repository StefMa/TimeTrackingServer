# -*- coding: utf-8 -*-
import base64
import logging

class header_helper():
    def __init__(self, headers):
        self.debug_headers(headers)

        auth = headers["Authorization"].split(" ");
        self.basic_identifier = auth[0]
        self.basic_username = base64.b64decode(auth[1]).split(":")[0]
        self.basic_password = base64.b64decode(auth[1]).split(":")[1]

        self.supported_versions = ["1"]
        self.api_version = headers["TT-Api-Version"]

    # Check if BasicAuth valid
    # Return True if valid. False otherwise
    def valid_auth(self):
        if (self.basic_identifier == "Basic" and
            self.basic_username == "[USERNAME]" and
            self.basic_password == "[PASSWORD]"):
            return True
        return False

    # Check if 'TT-Api-Version' is valid
    # Return Api-Version if valid. None otherwise
    def valid_api_version(self):
        if self.api_version in self.supported_versions:
            return self.api_version
        return None

    def debug_headers(self, headers):
        logging.info("BasicAuth: " + headers["Authorization"])
        logging.info("TT-Api-Version: " + headers["TT-Api-Version"])
