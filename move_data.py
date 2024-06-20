import pymongo
import json
import os
from pymongo import MongoClient, InsertOne

# Connection to the MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('DB_NAME')
DB_COLLECTION = os.getenv('DB_COLLECTION')
client = pymongo.MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[DB_COLLECTION]
requesting = []

files = ['iphone', 'samsung', 'xiaomi']
for file in files:
    with open(f"data/{file}.json",'r', encoding='utf-8') as f:
        # for jsonObj in f:
        myDict = json.load(f)
        for item in myDict['items']:
            requesting.append(InsertOne(item))
            print(item)
            print('-------------------')
            

result = collection.bulk_write(requesting)
client.close()