#create a function that checks if user email and phone number is in mongoDB databse
import pymongo

def validate_user_lost_account(email, phone_number):
    collection = db_Account()
    #check if email and phone number is in database
    if collection.find_one({"Email": email, "Phone": phone_number}):
       return collection.find_one({"Email": email, "Phone": phone_number},  { "RegistrationNum": 1, "PAC": 1, "_id": 0}) and True
    else:
        return False
