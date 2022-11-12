#install pymongo
#pip3 install pymongo

import pymongo
import json

class DB:
    #create a mongoclient object
    client = pymongo.MongoClient("mongodb://bank-kiosk:toff8AnPUDMuvsvTvE3Jqy1JuyoSxWzaxyJR8Om76blxHZW8Io0Lcqx4R76GQgpACixUCuyr3Q5XRCksbboS9A==@bank-kiosk.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@bank-kiosk@")

