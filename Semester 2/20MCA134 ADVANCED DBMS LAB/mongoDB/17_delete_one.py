from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Delete by rollno
col.delete_one({"rollno": 1})
print("\nDeleted student with rollno = 1")

# 2. Delete by name
col.delete_one({"name": "Rahul"})
print("\nDeleted student with name Rahul")

# 3. Delete with condition (marks < 40)
col.delete_one({"marks": {"$lt": 40}})
print("\nDeleted one student with low marks")

# 4. Delete using AND condition
col.delete_one({
    "$and": [
        {"marks": {"$gt": 80}},
        {"name": "Akhil"}
    ]
})
print("\nDeleted one matching AND condition")

# 5. Show remaining data
print("\nRemaining Documents:")
for doc in col.find():
    print(doc)