from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["Akhil"]

print("Collections in Akhil DB:")
for col in db.list_collection_names():
    print(col)