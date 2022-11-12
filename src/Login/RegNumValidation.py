# check that a parameter is 9 in length, first 3 characters are alphabetic the rest are numbers
def validateRegNum(regNum):
    import re
    if re.match(r'^[a-zA-Z]{3}\d{6}$', regNum):
        return True
    else:
        return False
