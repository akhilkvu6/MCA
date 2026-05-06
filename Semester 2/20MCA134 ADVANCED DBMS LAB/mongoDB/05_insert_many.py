from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

data = [
    {"rollno": 2, "name": "Rahul", "marks": 70},
    {"rollno": 3, "name": "John", "marks": 85}
]

col.insert_many(data)

print("Multiple data inserted")