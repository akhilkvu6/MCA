from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Show only name
print("\nOnly name:")
for doc in col.find({}, {"name": 1}):
    print(doc)

# 2. Show name and marks
print("\nName and marks:")
for doc in col.find({}, {"name": 1, "marks": 1}):
    print(doc)

# 3. Hide _id
print("\nWithout _id:")
for doc in col.find({}, {"name": 1, "marks": 1, "_id": 0}):
    print(doc)

# 4. Show only rollno
print("\nOnly rollno:")
for doc in col.find({}, {"rollno": 1, "_id": 0}):
    print(doc)

# 5. Show all except marks
print("\nAll except marks:")
for doc in col.find({}, {"marks": 0}):
    print(doc)

# 6. Show only name for marks > 80
print("\nName where marks > 80:")
for doc in col.find({"marks": {"$gt": 80}}, {"name": 1, "_id": 0}):
    print(doc)

# 7. Multiple fields with condition
print("\nName + marks where rollno < 5:")
for doc in col.find({"rollno": {"$lt": 5}}, {"name": 1, "marks": 1, "_id": 0}):
    print(doc)