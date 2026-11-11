import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Create database and collection
db = client["Akhil"]
col = db["students"]

# Open JSON file
with open("test.json", "r") as file:
    data = json.load(file)

# Insert data into MongoDB
col.insert_many(data)

print("✅ JSON data imported successfully")