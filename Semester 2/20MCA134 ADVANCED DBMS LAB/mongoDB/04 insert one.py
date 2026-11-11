from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

col.insert_one({
    "rollno": 1,
    "name": "Akhil",
    "marks": 85
})

print("Data inserted")