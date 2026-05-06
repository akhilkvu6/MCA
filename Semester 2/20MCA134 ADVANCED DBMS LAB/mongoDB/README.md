# 🍃 MongoDB Programs using Python (PyMongo)

## 📖 Overview

This folder contains MongoDB programs implemented using Python and PyMongo as part of the **20MCA134 Advanced DBMS Lab**.

The programs demonstrate:

- MongoDB Connection
- CRUD Operations
- Query Processing
- Projection Queries
- Sorting & Limiting
- Operators & Conditional Queries
- Regular Expressions
- Update & Delete Operations
- JSON Import
- Mini Projects

---

# 🛠 Requirements

Install PyMongo before running the programs.

```bash
pip install pymongo
```

---

# ▶ Running Programs

```bash
python filename.py
```

Example:

```bash
python 01_connect.py
```

---

# 📂 Program List

| No | Program | Description |
|----|----------|-------------|
| 01 | `01_connect.py` | Connects Python with MongoDB server |
| 02 | `02_list_databases.py` | Displays all databases in MongoDB |
| 03 | `03_list_collections.py` | Displays collections inside a database |
| 04 | `04_insert_one.py` | Inserts a single document into MongoDB |
| 05 | `05_insert_many.py` | Inserts multiple documents |
| 06 | `06_find_all.py` | Retrieves all documents from collection |
| 07 | `07_find_one.py` | Retrieves a single document |
| 08 | `08_find_filter.py` | Demonstrates filtering queries and operators |
| 09 | `09_find_projection.py` | Displays selected fields using projection |
| 10 | `10_find_sort.py` | Sorts documents in ascending/descending order |
| 11 | `11_find_limit.py` | Limits the number of retrieved documents |
| 12 | `12_find_operators.py` | Demonstrates MongoDB query operators |
| 13 | `13_find_and_or.py` | Demonstrates AND & OR conditional queries |
| 14 | `14_find_regex.py` | Demonstrates Regular Expression queries |
| 15 | `15_update_one.py` | Updates a single document |
| 16 | `16_update_many.py` | Updates multiple documents |
| 17 | `17_delete_one.py` | Deletes a single document |
| 18 | `18_delete_many.py` | Deletes multiple documents |
| 19 | `19_student_project.py` | Mini project for student management |
| 20 | `20_student_advanced_project.py` | Advanced student management system |
| 21 | `21_import_from_json.py` | Imports JSON data into MongoDB |
| — | `test.json` | Sample JSON dataset used for import |

---

# 📚 Program Explanations

---

## 01_connect.py

### Purpose
Connects Python to the MongoDB server using PyMongo.

### Code

```python
import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")

print("Connected successfully")
```

### Explanation
- `MongoClient()` establishes connection with MongoDB server.
- `localhost:27017` is the default MongoDB address.
- Displays success message after connection.

---

## 02_list_databases.py

### Purpose
Displays all databases available in MongoDB.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

print("Databases:")
for db in client.list_database_names():
    print(db)
```

### Explanation
- `list_database_names()` returns all database names.
- Loop prints each database.

---

## 03_list_collections.py

### Purpose
Displays collections inside a database.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["Akhil"]

print("Collections in Akhil DB:")
for col in db.list_collection_names():
    print(col)
```

### Explanation
- Selects database `Akhil`.
- `list_collection_names()` retrieves all collections.

---

## 04_insert_one.py

### Purpose
Inserts a single document into MongoDB collection.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

col.insert_one({
    "rollno": 1,
    "name": "Akhil",
    "marks": 85
})

print("Data inserted")
```

### Explanation
- `insert_one()` inserts one document into collection.
- MongoDB automatically creates collection if it doesn't exist.

---

## 05_insert_many.py

### Purpose
Inserts multiple documents into collection.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

data = [
    {"rollno": 2, "name": "Rahul", "marks": 70},
    {"rollno": 3, "name": "John", "marks": 85}
]

col.insert_many(data)

print("Multiple data inserted")
```

### Explanation
- `insert_many()` inserts multiple documents at once.
- Data is passed as list of dictionaries.

---

## 06_find_all.py

### Purpose
Retrieves all documents from collection.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

for doc in col.find():
    print(doc)
```

### Explanation
- `find()` retrieves all documents.
- Loop displays each document.

---

## 07_find_one.py

### Purpose
Retrieves one document from collection.

### Code

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["table1"]

doc = col.find_one()
print(doc)
```

### Explanation
- `find_one()` returns the first matching document.

---

## 08_find_filter.py

### Purpose
Demonstrates filtering using MongoDB query operators.

### Topics Covered
- Equal
- Greater than
- Less than
- AND / OR
- IN / NOT
- Regex

### Explanation
Uses conditional operators like:
- `$gt`
- `$lt`
- `$gte`
- `$lte`
- `$ne`
- `$in`
- `$and`
- `$or`

to filter documents.

---

## 09_find_projection.py

### Purpose
Displays selected fields from documents.

### Explanation
Projection is used to:
- include fields
- exclude fields
- hide `_id`

Example:

```python
col.find({}, {"name": 1, "_id": 0})
```

---

## 10_find_sort.py

### Purpose
Sorts MongoDB documents.

### Explanation
Uses:

```python
.sort("marks", 1)
```

- `1` → ascending
- `-1` → descending

---

## 11_find_limit.py

### Purpose
Limits number of documents retrieved.

### Explanation

```python
.limit(2)
```

Returns only first 2 documents.

---

## 12_find_operators.py

### Purpose
Demonstrates MongoDB query operators.

### Operators Used
- `$gt`
- `$lt`
- `$gte`
- `$lte`
- `$ne`
- `$in`
- `$nin`

---

## 13_find_and_or.py

### Purpose
Demonstrates logical queries.

### Explanation
Uses:
- `$and`
- `$or`

for combining conditions.

---

## 14_find_regex.py

### Purpose
Performs Regular Expression queries.

### Example

```python
{"name": {"$regex": "^A"}}
```

Matches names starting with A.

---

## 15_update_one.py

### Purpose
Updates a single document.

### Methods Used
- `$set`
- `$inc`

### Explanation
Updates marks, name, and fields of one document.

---

## 16_update_many.py

### Purpose
Updates multiple documents.

### Explanation
Uses `update_many()` for bulk updates.

---

## 17_delete_one.py

### Purpose
Deletes one document from collection.

### Explanation
Uses:

```python
delete_one()
```

to remove single matching document.

---

## 18_delete_many.py

### Purpose
Deletes multiple documents.

### Explanation
Uses:

```python
delete_many()
```

for bulk deletion.

---

## 19_student_project.py

### Purpose
Mini project for student management.

### Features
- Add student
- View all students
- Search student
- Update marks
- Delete student

### Explanation
Menu-driven MongoDB CRUD application using Python.

---

## 20_student_advanced_project.py

### Purpose
Advanced student database project.

### Features
- Topper calculation
- Regex search
- Student count
- Total marks
- Conditional filtering

### Explanation
Advanced MongoDB operations combined into single application.

---

## 21_import_from_json.py

### Purpose
Imports JSON dataset into MongoDB.

### Code

```python
import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["Akhil"]
col = db["students"]

with open("test.json", "r") as file:
    data = json.load(file)

col.insert_many(data)

print("JSON data imported successfully")
```

### Explanation
- Reads JSON data using `json.load()`
- Imports data into MongoDB collection
- Demonstrates JSON handling with MongoDB

---

# 📦 Sample Dataset

## test.json

Contains sample student records in JSON format for import demonstration.

---

# 🧠 Concepts Covered

✅ MongoDB Connection  
✅ CRUD Operations  
✅ Query Operators  
✅ Projection Queries  
✅ Sorting & Limiting  
✅ Regex Queries  
✅ Update & Delete Operations  
✅ JSON Import  
✅ Mini Projects  

---

# 💻 Technologies Used

- Python
- MongoDB
- PyMongo
- JSON

---

# 👨‍💻 Author

## Akhil Krishna

MCA Student • Developer • Tech Enthusiast

---