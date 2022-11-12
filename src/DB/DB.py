#install pymongo
#pip3 install pymongo

import pymongo
from pymongo import MongoClient

def db_connect():
    #create a mongoclient object
    client = MongoClient(
        'mongodb://kioskmoney:qiaccMve6KMXf8d3hK5yhvHwR9Hblzw3pN5ANkSvfP1bkC9rrRVn7qm1487vdo58ZZVe3HdDtX2hACDbmzfgPg==@kioskmoney.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@kioskmoney@',
        27017)
    return client

def db_Account():
    client = db_connect()
    db = client['Kiosk']
    collection = db['Account']
    return collection

def db_Holding():
    client = db_connect()
    db = client['Kiosk']
    collection = db['Holding']
    return collection