from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Equal
print("\nEqual (marks = 85):")
for doc in col.find({"marks": 85}):
    print(doc)

# 2. Greater than
print("\nMarks > 80:")
for doc in col.find({"marks": {"$gt": 80}}):
    print(doc)

# 3. Less than
print("\nMarks < 80:")
for doc in col.find({"marks": {"$lt": 80}}):
    print(doc)

# 4. Greater than or equal
print("\nMarks >= 80:")
for doc in col.find({"marks": {"$gte": 80}}):
    print(doc)

# 5. Less than or equal
print("\nMarks <= 80:")
for doc in col.find({"marks": {"$lte": 80}}):
    print(doc)

# 6. Not equal
print("\nMarks != 80:")
for doc in col.find({"marks": {"$ne": 80}}):
    print(doc)

# 7. AND condition
print("\nMarks between 70 and 90:")
for doc in col.find({
    "$and": [
        {"marks": {"$gt": 70}},
        {"marks": {"$lt": 90}}
    ]
}):
    print(doc)

# 8. OR condition
print("\nMarks = 85 OR Marks = 90:")
for doc in col.find({
    "$or": [
        {"marks": 85},
        {"marks": 90}
    ]
}):
    print(doc)

# 9. NOT condition
print("\nNOT marks = 85:")
for doc in col.find({"marks": {"$not": {"$eq": 85}}}):
    print(doc)

# 10. IN condition
print("\nMarks in [85, 90]:")
for doc in col.find({"marks": {"$in": [85, 90]}}):
    print(doc)

# 11. REGEX (starts with A)
print("\nName starts with A:")
for doc in col.find({"name": {"$regex": "^A"}}):
    print(doc)