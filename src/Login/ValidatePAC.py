
# make a method to check if a parameter is a valid pac
def validatePAC(pac):
    import re
    if re.match(r'^\d{8}$', pac):
        return True
    else:
        return False
