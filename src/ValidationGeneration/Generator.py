import random

# crate a random registration String letter and 4 numbers
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

# make a method to generate a random string 8 numbers in length
def generatePAC():
    import random
    import string
    pac = ''.join(random.choice(string.digits) for _ in range(8))
    return pac