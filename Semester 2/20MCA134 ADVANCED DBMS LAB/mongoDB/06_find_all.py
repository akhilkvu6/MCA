from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

for doc in col.find():
    print(doc)