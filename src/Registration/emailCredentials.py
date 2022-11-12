#def that connects to the database and returns the collection object
import sys
sys.path.append("D:\a\1\s\src\DB")
import DB

def emailCredentials(email, phone_number):
    collections = DB.db_Account()
    #find registration and PAC code in database
    for x in collections.find({"email": email, "phoneNumber": phone_number}, {"_id": 0, "regNumber": 1, "PAC": 1}):
        userLoginDetails = x
    emailCredentials(email, userLoginDetails)








