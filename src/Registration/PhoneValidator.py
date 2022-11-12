#class that check number is irish format or not

import re

def phoneValid(phoneNumber):
    phoneNumber.strip()
    if re.search(r'^\+353\d{9}$', phoneNumber):
        return True
    elif re.search(r'^0\d{9}$', phoneNumber):
        return True
    else:
        return False


