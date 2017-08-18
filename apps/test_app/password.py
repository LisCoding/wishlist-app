import re

class PasswordLenChecker(object):
    def __init__(self, passwd, l):
        if len(passwd) < l:
         raise ValueError("Password has to be a least " + str(l) + " characters")

class PasswordDigitChecker(object):
    def __init__(self, str):
        if not re.search("\d", str):
            raise ValueError("Password need to have a least one digit")

class PasswordUppercaseChecker(object):
    def __init__(self, str):
        if bool(re.match(r'[A-Z]+$', str)):
            raise ValueError("Password need to have a least one digit")

class Password(object):
    def __init__(self, pass1, pass2):
        PasswordLenChecker(pass1, 8)
        if not pass1 == pass2:
            raise ValueError("Password and confirmation password does not match")

        PasswordDigitChecker(pass1)
        PasswordUppercaseChecker(pass1)
