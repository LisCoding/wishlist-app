class EmptyFieldChecker(object):
    def __init__(self, str, field_name):
        if len(str) == 0:
            raise ValueError("Field " + field_name + " can not be empty")
        elif len(str) < 3:
            raise ValueError("Field " + field_name + " has to be at least 2 letters")

class Name(object):
    def __init__(self, fname, lname):
        EmptyFieldChecker(fname, "first name")
        EmptyFieldChecker(lname, "last name")
        if fname.isalpha() == False or lname.isalpha() == False:
            raise ValueError("Name and Last name should contain only alpha characters")
        self.fname = fname
        self.lname = lname
