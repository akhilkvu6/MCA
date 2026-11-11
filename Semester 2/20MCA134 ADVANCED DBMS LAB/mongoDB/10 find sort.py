from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Sort by marks ascending
print("\nMarks ascending:")
for doc in col.find().sort("marks", 1):
    print(doc)

# 2. Sort by marks descending
print("\nMarks descending:")
for doc in col.find().sort("marks", -1):
    print(doc)

# 3. Sort by name ascending
print("\nName ascending:")
for doc in col.find().sort("name", 1):
    print(doc)

# 4. Sort by name descending
print("\nName descending:")
for doc in col.find().sort("name", -1):
    print(doc)

# 5. Sort with projection
print("\nName + marks sorted by marks:")
for doc in col.find({}, {"name": 1, "marks": 1, "_id": 0}).sort("marks", -1):
    print(doc)

# 6. Sort with condition
print("\nMarks > 70 sorted descending:")
for doc in col.find({"marks": {"$gt": 70}}).sort("marks", -1):
    print(doc)

# 7. Sort multiple fields (first marks, then name)
print("\nSort by marks then name:")
for doc in col.find({}, {"name": 1, "marks": 1, "_id": 0}).sort([
    ("marks", -1),
    ("name", 1)
]):
    print(doc)