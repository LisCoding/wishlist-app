import re

class Email(object):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    def __init__(self, email):
        if not self.EMAIL_REGEX.match(email):
            raise ValueError("Invalid Email Address!")
        self.email = email
