# crate a random registration String letter and 4 numbers

import random
import re

def RegistrationGen():
    # create a string of letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # create a random string of letters
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    # create a random number
    number = random.randint(100000, 999999)
    # create a random registration number
    return letter1 + letter2 + letter3 +str(number)


# regex to check if registration number is valid
def RegistrationValid(registrationNumber):
    registrationNumber.strip()
    if re.search(r'^[A-Z]{3}\d{6}$', registrationNumber):
        return True
    else:
        return False

