from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Greater than
print("\nMarks > 80:")
for doc in col.find({"marks": {"$gt": 80}}):
    print(doc)

# 2. Less than
print("\nMarks < 80:")
for doc in col.find({"marks": {"$lt": 80}}):
    print(doc)

# 3. Greater than or equal
print("\nMarks >= 80:")
for doc in col.find({"marks": {"$gte": 80}}):
    print(doc)

# 4. Less than or equal
print("\nMarks <= 80:")
for doc in col.find({"marks": {"$lte": 80}}):
    print(doc)

# 5. Not equal
print("\nMarks != 80:")
for doc in col.find({"marks": {"$ne": 80}}):
    print(doc)

# 6. IN (multiple values)
print("\nMarks in [70, 85, 90]:")
for doc in col.find({"marks": {"$in": [70, 85, 90]}}):
    print(doc)

# 7. NOT IN
print("\nMarks not in [70, 85]:")
for doc in col.find({"marks": {"$nin": [70, 85]}}):
    print(doc)

# 8. AND condition
print("\nMarks between 70 and 90:")
for doc in col.find({
    "$and": [
        {"marks": {"$gt": 70}},
        {"marks": {"$lt": 90}}
    ]
}):
    print(doc)

# 9. OR condition
print("\nMarks = 85 OR 90:")
for doc in col.find({
    "$or": [
        {"marks": 85},
        {"marks": 90}
    ]
}):
    print(doc)

# 10. NOT condition
print("\nNOT marks = 80:")
for doc in col.find({"marks": {"$not": {"$eq": 80}}}):
    print(doc)