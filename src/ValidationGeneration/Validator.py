import re

# make a method to check if a parameter is a valid pac
def validatePAC(pac):
    if re.match(r'^\d{8}$', pac):
        return True
    else:
        return False

# check that a parameter is 9 in length, first 3 characters are alphabetic the rest are numbers
def validateRegNum(regNum):
    if re.match(r'^[a-zA-Z]{3}\d{6}$', regNum):
        return True
    else:
        return False

# regex to check if registration number is valid
def RegistrationValid(registrationNumber):
    registrationNumber.strip()
    if re.search(r'^[A-Z]{3}\d{6}$', registrationNumber):
        return True
    else:
        return False

#class that check number is irish format or not
def phoneValid(phoneNumber):
    phoneNumber.strip()
    if re.search(r'^\+353\d{9}$', phoneNumber):
        return True
    elif re.search(r'^0\d{9}$', phoneNumber):
        return True
    else:
        return False

#this class will validate the name of the user
def nameValid(firstName):
    if len(firstName) < 2 or len(firstName) > 20:
        return False
    if firstName.isalpha() == False:
        return False
    if " " in firstName:
        return False
    return True

#function to validate two values are the same
def validateEmailCode(sentCode, UserinputCode):
    if sentCode == UserinputCode:
        return True
    else:
        return False