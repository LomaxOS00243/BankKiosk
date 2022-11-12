#class to check IBAN is valid or not

import re

def IBANValid(IBAN):
    IBAN.strip()
    if re.search(r'^IE\d{2}[A-Z]{4}\d{14}$', IBAN):
        return True
    else:
        return False

