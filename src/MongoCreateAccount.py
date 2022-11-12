import pymongo
from pymongo import MongoClient

def createAccount(firstName, lastName, registrationNumber, PAC, email, phoneNumber, Eircode, IBAN):
    try:
        account = db_Account()
        account.insert_one({"FirstName": firstName, "LastName": lastName, "RegistrationNum": registrationNumber, "PAC": PAC, "Email": email, "Phone": phoneNumber, "EIRCODE": Eircode, "IBAN": IBAN},{"_id": 1})
        return True
    except:
        return False
