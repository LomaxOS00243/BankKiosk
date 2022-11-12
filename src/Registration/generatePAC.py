# make a method to generate a random string 8 numbers in length
def generatePAC():
    import random
    import string
    pac = ''.join(random.choice(string.digits) for _ in range(8))
    return pac


