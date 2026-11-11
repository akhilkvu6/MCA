from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Update all students with marks < 50
col.update_many(
    {"marks": {"$lt": 50}},
    {"$set": {"status": "fail"}}
)
print("\nUpdated all students with marks < 50")

# 2. Increase marks for all students
col.update_many(
    {},
    {"$inc": {"marks": 5}}
)
print("\nIncreased marks for all students")

# 3. Add new field to all
col.update_many(
    {},
    {"$set": {"semester": "S2"}}
)
print("\nAdded semester field to all")

# 4. Update multiple based on condition
col.update_many(
    {"marks": {"$gt": 80}},
    {"$set": {"grade": "A"}}
)
print("\nUpdated grade A for high scorers")

# 5. Remove a field from all documents
col.update_many(
    {},
    {"$unset": {"semester": ""}}
)
print("\nRemoved semester field")

# 6. Show updated data
print("\nAll Documents:")
for doc in col.find():
    print(doc)