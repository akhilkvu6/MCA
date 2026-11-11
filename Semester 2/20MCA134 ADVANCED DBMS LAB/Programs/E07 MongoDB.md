# EXERCISE 7: MongoDB

## Aim

To create a MongoDB database named `college`, create a collection named `studlist`, insert student records from a JSON file, and perform various MongoDB queries using Python and PyMongo.

---

# Filename

```text id="u30pc5"
E07_MongoDB.py
```

---

# Concepts Used

* MongoDB
* NoSQL Database
* PyMongo
* JSON File Handling
* Collections and Documents
* MongoDB Query Operators
* Filtering and Projection
* Sorting and Limiting
* Regular Expressions

---

# Software Requirements

| Software          | Purpose               |
| ----------------- | --------------------- |
| MongoDB           | Database Server       |
| Python            | Programming Language  |
| PyMongo           | MongoDB Python Driver |
| VS Code / PyCharm | IDE                   |

---

# Theory

## MongoDB

MongoDB is a NoSQL document-oriented database that stores data in JSON-like BSON format. Unlike relational databases, MongoDB stores data as collections and documents instead of tables and rows.

MongoDB is widely used for:

* Large scale applications
* Real-time analytics
* Flexible schema applications
* Big data storage

---

## Collection

A collection in MongoDB is similar to a table in relational databases. It stores multiple documents.

Example:

```json id="z9x6tt"
{
    "name":"Akhil",
    "course":"MCA"
}
```

---

## Document

A document is a single record stored inside a collection.

MongoDB documents are stored in BSON format.

---

## PyMongo

PyMongo is the official Python library used to connect Python applications with MongoDB databases.

Installation:

```bash id="20l91o"
pip install pymongo
```

---

# Source Code

```python id="x9ks4n"
# EXERCISE 7: MongoDB

import pymongo
import json

conn = pymongo.MongoClient("mongodb://localhost:27017/")

db = conn['college']

col = db['studlist']

with open("data.json") as file:
    data = json.load(file)

db.studlist.insert_many(data)

print("Records inserted successfully")

print("\n1. Female students in MCA")

x = db.studlist.find(
    {"gender":"female","course":"MCA"},
    {"name":1,"mark":1}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'], "| Mark:", i['mark'])

print("\n2. Highest mark in MCA")

x = db.studlist.find(
    {"course":"MCA"}
).sort("mark",-1).limit(1)

for i in x:
    print(i)

print("\n3. Male students with A+ grade")

x = db.studlist.find(
    {"grade":"A+","gender":"male"}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'])

print("\n4. Top 3 students in Mechanical department")

x = db.studlist.find(
    {"course":"Mechanical"}
).sort("mark",-1).limit(3)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'], "| Mark:", i['mark'])

print("\n5. Female students with marks greater than 90")

x = db.studlist.find(
    {"mark":{"$gt":90},"gender":"female"}
)

for i in x:
    print(
        "Name:", i['name']['fname'], i['name']['lname'],
        "| Grade:", i['grade'],
        "| Mark:", i['mark'],
        "| Contact:", i['phone']['no']
    )

print("\n6. Students with marks between 80 and 90")

x = db.studlist.find(
    {"mark":{"$gt":80,"$lt":90}}
)

for i in x:
    print(
        "Name:", i['name']['fname'], i['name']['lname'],
        "| Grade:", i['grade'],
        "| Mark:", i['mark'],
        "| Contact:", i['phone']['no']
    )

print("\n7. Students whose name starts with V")

x = db.studlist.find(
    {"name.fname":{"$regex":"^V"}}
)

for i in x:
    print(
        "Name:", i['name']['fname'], i['name']['lname'],
        "| Course:", i['course'],
        "| Grade:", i['grade'],
        "| Mark:", i['mark'],
        "| Contact:", i['phone']['no']
    )

print("\n8. Students from Kollam")

x = db.studlist.find(
    {"address.city":"Kollam"}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'])

print("\n9. Students not from Kollam or Thiruvananthapuram")

x = db.studlist.find(
    {
        "address.city":
        {
            "$nin":["Kollam","Thiruvananthapuram"]
        }
    }
)

for i in x:
    print(
        "Name:", i['name']['fname'], i['name']['lname'],
        "| City:", i['address']['city']
    )

print("\n10. Female students from Kollam or Thiruvananthapuram")

x = db.studlist.find(
    {
        "gender":"female",
        "address.city":
        {
            "$in":["Kollam","Thiruvananthapuram"]
        }
    }
)

for i in x:
    print(
        "Name:", i['name']['fname'], i['name']['lname'],
        "| City:", i['address']['city']
    )
```

---

# Sample data.json File

```json id="8h63g7"
[
    {
        "name":
        {
            "fname":"Anu",
            "lname":"Raj"
        },
        "gender":"female",
        "course":"MCA",
        "mark":95,
        "grade":"A+",
        "phone":
        {
            "no":"9876543210"
        },
        "address":
        {
            "city":"Kollam"
        }
    },
    {
        "name":
        {
            "fname":"Vishnu",
            "lname":"Kumar"
        },
        "gender":"male",
        "course":"Mechanical",
        "mark":88,
        "grade":"A",
        "phone":
        {
            "no":"9123456780"
        },
        "address":
        {
            "city":"Thrissur"
        }
    }
]
```

---

# MongoDB Operators Used

| Operator | Meaning              |
| -------- | -------------------- |
| `$gt`    | Greater than         |
| `$lt`    | Less than            |
| `$in`    | Value exists in list |
| `$nin`   | Value not in list    |
| `$regex` | Pattern matching     |

---

# Algorithm

1. Import `pymongo` and `json`.
2. Connect Python with MongoDB server.
3. Create database `college`.
4. Create collection `studlist`.
5. Read student data from `data.json`.
6. Insert records into collection.
7. Execute MongoDB queries using filters and operators.
8. Display matching results.

---

# Flow of Execution

```text id="s6g5jn"
Start
   ↓
Connect to MongoDB
   ↓
Create Database
   ↓
Create Collection
   ↓
Read JSON File
   ↓
Insert Records
   ↓
Execute Queries
   ↓
Display Output
   ↓
Stop
```

---

# Important MongoDB Functions

| Function        | Purpose                   |
| --------------- | ------------------------- |
| `find()`        | Retrieve documents        |
| `insert_many()` | Insert multiple documents |
| `sort()`        | Sort documents            |
| `limit()`       | Limit number of documents |

---

# Internal Working

* Python connects to MongoDB using `MongoClient`.
* MongoDB automatically creates database and collection if they do not exist.
* JSON data is converted into MongoDB documents.
* Query operators filter matching records.
* Results are displayed using loops.

---

# Time Complexity

## Database Search Operations

| Operation    | Complexity  |
| ------------ | ----------- |
| Simple Find  | O(n)        |
| Sorted Query | O(n \log n) |
| Regex Search | O(n)        |

Where:

* `n` = number of documents in collection

---

# Space Complexity

O(n)

Additional space is required for storing records and query results.

---

# Advantages

* Flexible schema
* Easy data storage
* Faster development
* Simple JSON structure
* Good scalability
* Supports large datasets

---

# Limitations

* High memory usage
* Complex joins are difficult
* Less strict schema validation

---

# Edge Cases

* Empty collection
* Invalid JSON format
* Missing fields in documents
* No matching query results
* MongoDB server not running

---

# Possible Improvements

* Add menu-driven interface
* Add exception handling
* Use aggregation framework
* Add indexing for faster queries
* Develop GUI frontend

---

# Possible Errors and Exceptions

| Error             | Cause                      |
| ----------------- | -------------------------- |
| Connection Error  | MongoDB server not running |
| FileNotFoundError | Missing JSON file          |
| JSONDecodeError   | Invalid JSON structure     |
| KeyError          | Missing document field     |

---

# Sample Output

```text id="pxv7u8"
1. Female students in MCA
Name: Anu Raj | Mark: 95

2. Highest mark in MCA
{'name': {'fname': 'Anu', 'lname': 'Raj'}, 'mark': 95}

3. Male students with A+ grade

4. Top 3 students in Mechanical department
Name: Vishnu Kumar | Mark: 88
```

---

# Viva Questions and Answers

## 1. What is MongoDB?

MongoDB is a NoSQL document-oriented database.

---

## 2. What is a collection?

A collection is a group of MongoDB documents.

---

## 3. What is BSON?

BSON stands for Binary JSON used internally by MongoDB.

---

## 4. What is PyMongo?

PyMongo is the Python driver for MongoDB.

---

## 5. What is the use of `find()`?

`find()` retrieves documents matching specified conditions.

---

## 6. Explain `$gt`.

`$gt` means greater than.

Example:

```python id="1xw8np"
{"mark":{"$gt":90}}
```

---

## 7. What is projection?

Projection selects specific fields from documents.

---

## 8. Explain `$regex`.

`$regex` is used for pattern matching.

---

## 9. Difference between SQL and MongoDB?

| SQL              | MongoDB         |
| ---------------- | --------------- |
| Table-based      | Document-based  |
| Fixed schema     | Flexible schema |
| Rows and columns | JSON documents  |

---

## 10. What is a document?

A document is a single JSON-like record stored in MongoDB.

---

# GitHub Workflow

```bash id="1m9gpo"
git add "Semester 2/20MCA134 ADVANCED DBMS LAB/Programs/E07_MongoDB.py" "Semester 2/20MCA134 ADVANCED DBMS LAB/Programs/README.md"

git commit -m "Added Exercise 07 - MongoDB"

git push
```

---

# Result

Thus the MongoDB database `college` and collection `studlist` were created successfully, records were inserted from a JSON file, and various MongoDB queries were executed successfully using Python and PyMongo.
