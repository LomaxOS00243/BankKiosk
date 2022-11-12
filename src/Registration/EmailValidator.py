#class for checking if user email is valid email

import re

def emailValid(email):
    email.strip()
    if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    else:
        return False

