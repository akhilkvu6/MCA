from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. AND condition (marks between 70 and 90)
print("\nAND: Marks between 70 and 90:")
for doc in col.find({
    "$and": [
        {"marks": {"$gt": 70}},
        {"marks": {"$lt": 90}}
    ]
}):
    print(doc)

# 2. OR condition (marks = 85 or 90)
print("\nOR: Marks = 85 or 90:")
for doc in col.find({
    "$or": [
        {"marks": 85},
        {"marks": 90}
    ]
}):
    print(doc)

# 3. AND with names
print("\nAND: Name = Akhil AND marks > 80:")
for doc in col.find({
    "$and": [
        {"name": "Akhil"},
        {"marks": {"$gt": 80}}
    ]
}):
    print(doc)

# 4. OR with names
print("\nOR: Name = Akhil OR Rahul:")
for doc in col.find({
    "$or": [
        {"name": "Akhil"},
        {"name": "Rahul"}
    ]
}):
    print(doc)

# 5. Combined AND + OR
print("\nCombined AND + OR:")
for doc in col.find({
    "$and": [
        {"marks": {"$gt": 70}},
        {
            "$or": [
                {"name": "Akhil"},
                {"name": "John"}
            ]
        }
    ]
}):
    print(doc)

# 6. AND with projection
print("\nAND with projection (name + marks):")
for doc in col.find(
    {"$and": [{"marks": {"$gt": 70}}, {"marks": {"$lt": 90}}]},
    {"name": 1, "marks": 1, "_id": 0}
):
    print(doc)

# 7. OR with sort
print("\nOR with sorting:")
for doc in col.find({
    "$or": [{"marks": 85}, {"marks": 90}]
}).sort("marks", -1):
    print(doc)