from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

# 1. Starts with A
print("\nStarts with A:")
for doc in col.find({"name": {"$regex": "^A"}}):
    print(doc)

# 2. Ends with a
print("\nEnds with a:")
for doc in col.find({"name": {"$regex": "a$"}}):
    print(doc)

# 3. Contains 'ar'
print("\nContains 'ar':")
for doc in col.find({"name": {"$regex": "ar"}}):
    print(doc)

# 4. Case insensitive (A or a)
print("\nCase insensitive (a):")
for doc in col.find({"name": {"$regex": "a", "$options": "i"}}):
    print(doc)

# 5. Starts with A and ends with l
print("\nStarts A and ends l:")
for doc in col.find({"name": {"$regex": "^A.*l$"}}):
    print(doc)

# 6. Exact match
print("\nExact match (Akhil):")
for doc in col.find({"name": {"$regex": "^Akhil$"}}):
    print(doc)

# 7. Names with 5 letters
print("\nExactly 5 letters:")
for doc in col.find({"name": {"$regex": "^.{5}$"}}):
    print(doc)

# 8. Starts with vowel
print("\nStarts with vowel:")
for doc in col.find({"name": {"$regex": "^[AEIOUaeiou]"}}):
    print(doc)

# 9. Ends with vowel
print("\nEnds with vowel:")
for doc in col.find({"name": {"$regex": "[AEIOUaeiou]$"}}):
    print(doc)

# 10. Names without numbers
print("\nOnly letters (no numbers):")
for doc in col.find({"name": {"$regex": "^[A-Za-z]+$"}}):
    print(doc)

# 11. Names with digits
print("\nContains digits:")
for doc in col.find({"name": {"$regex": "[0-9]"}}):
    print(doc)