#this class will validate the name of the user

def nameValid(firstName):
    if type(Name) != str:
        return False
    if not Name.isalpha():
        return False
    if len(Name) < 2 or len(Name) > 20:
        return False
    return True

