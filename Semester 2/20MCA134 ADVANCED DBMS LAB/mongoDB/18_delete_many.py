from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Delete all students with marks < 50
col.delete_many({"marks": {"$lt": 50}})
print("\nDeleted students with marks < 50")

# 2. Delete by name (multiple)
col.delete_many({"name": "Rahul"})
print("\nDeleted all students named Rahul")

# 3. Delete using IN
col.delete_many({"marks": {"$in": [70, 80]}})
print("\nDeleted students with marks 70 or 80")

# 4. Delete using regex (name starts with A)
col.delete_many({"name": {"$regex": "^A"}})
print("\nDeleted names starting with A")

# 5. Delete ALL documents (⚠️ careful)
# col.delete_many({})
# print("\nDeleted ALL documents")

# 6. Show remaining data
print("\nRemaining Documents:")
for doc in col.find():
    print(doc)