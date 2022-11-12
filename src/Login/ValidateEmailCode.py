#function to validate two values are the same
def validateEmailCode(sentCode, UserinputCode):
    if sentCode == UserinputCode:
        return True
    else:
        return False