from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Limit first 2 documents
print("\nFirst 2 documents:")
for doc in col.find().limit(2):
    print(doc)

# 2. Limit first 3 documents
print("\nFirst 3 documents:")
for doc in col.find().limit(3):
    print(doc)

# 3. Sort + Limit (Top 2 highest marks)
print("\nTop 2 students (highest marks):")
for doc in col.find().sort("marks", -1).limit(2):
    print(doc)

# 4. Sort + Limit (Lowest 2 marks)
print("\nLowest 2 students:")
for doc in col.find().sort("marks", 1).limit(2):
    print(doc)

# 5. Projection + Limit
print("\nOnly name (limit 2):")
for doc in col.find({}, {"name": 1, "_id": 0}).limit(2):
    print(doc)

# 6. Filter + Limit
print("\nMarks > 70 (limit 2):")
for doc in col.find({"marks": {"$gt": 70}}).limit(2):
    print(doc)

# 7. Sort + Projection + Limit (Best practice combo)
print("\nTop 3 (name + marks only):")
for doc in col.find({}, {"name": 1, "marks": 1, "_id": 0}) \
              .sort("marks", -1) \
              .limit(3):
    print(doc)