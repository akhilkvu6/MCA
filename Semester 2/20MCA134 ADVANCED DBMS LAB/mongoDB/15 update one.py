from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Update marks for rollno = 1
col.update_one(
    {"rollno": 1},
    {"$set": {"marks": 95}}
)
print("\nUpdated marks for rollno 1")

# 2. Update name
col.update_one(
    {"rollno": 2},
    {"$set": {"name": "Rahul Kumar"}}
)
print("\nUpdated name")

# 3. Add new field (grade)
col.update_one(
    {"rollno": 1},
    {"$set": {"grade": "A"}}
)
print("\nAdded new field")

# 4. Increase marks (increment)
col.update_one(
    {"rollno": 1},
    {"$inc": {"marks": 5}}
)
print("\nMarks incremented")

# 5. Update only if condition matches
col.update_one(
    {"marks": {"$lt": 50}},
    {"$set": {"status": "fail"}}
)
print("\nUpdated low marks students")

# 6. Show updated data
print("\nUpdated Documents:")
for doc in col.find():
    print(doc)