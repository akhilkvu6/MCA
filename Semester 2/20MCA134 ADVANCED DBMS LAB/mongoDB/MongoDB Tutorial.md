# MongoDB with PyMongo Tutorial

> Complete reference guide for MongoDB operations using Python and PyMongo for Advanced DBMS Lab. 

---

# Table of Contents

1. Introduction to MongoDB
2. Features of MongoDB
3. MongoDB Terminologies
4. BSON
5. Installing MongoDB
6. Installing PyMongo
7. Connecting Python with MongoDB
8. Creating Database and Collection
9. CRUD Operations
10. Query Operators
11. Logical Operators
12. Regular Expressions
13. Update Operators
14. Aggregation Framework
15. Internal Working of PyMongo
16. Advantages and Limitations
17. Applications of MongoDB
18. Common Errors
19. Complexity Analysis
20. Viva Questions and Answers
21. Conclusion

---

# 1. Introduction to MongoDB

MongoDB is a NoSQL document-oriented database used to store data in flexible JSON-like documents called BSON (Binary JSON).

Unlike relational databases:

* MongoDB stores data as collections and documents
* Schema is flexible
* Tables and rows are replaced by collections and documents

MongoDB is widely used in:

* Web applications
* Real-time analytics
* Big data applications
* Cloud systems
* IoT systems

---

# 2. Features of MongoDB

* NoSQL database
* Schema-less design
* High performance
* Horizontal scalability
* BSON document storage
* Rich query language
* Aggregation framework support
* Indexing support
* Replication and sharding

---

# 3. MongoDB Terminologies

| SQL         | MongoDB    |
| ----------- | ---------- |
| Database    | Database   |
| Table       | Collection |
| Row         | Document   |
| Column      | Field      |
| Primary Key | `_id`      |

---

# 4. What is BSON?

BSON stands for Binary JSON.

MongoDB internally stores documents in BSON format for:

* Faster processing
* Efficient storage
* Easy traversal

## Example

```json id="p40g0o"
{
    "name":"Akhil",
    "course":"MCA",
    "mark":95
}
```

---

# 5. Installing MongoDB

## Step 1: Download MongoDB

Install MongoDB Community Server from:

```text id="jv2z7j"
https://www.mongodb.com/try/download/community
```

---

## Step 2: Verify Installation

```bash id="gy7jwy"
mongod --version
```

---

## Step 3: Start MongoDB Server

```bash id="3pp0n8"
mongod
```

---

# 6. Installing PyMongo

PyMongo is the official Python driver used to connect Python with MongoDB.

## Installation

```bash id="wwjj1r"
pip install pymongo
```

---

# 7. Importing PyMongo

```python id="5vq52x"
import pymongo
```

---

# 8. Connecting Python with MongoDB

```python id="7mjlwm"
import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
```

---

# 9. Creating Database

```python id="47mzrn"
db = conn['college']
```

MongoDB automatically creates the database when data is inserted.

---

# 10. Creating Collection

```python id="5y7d8v"
col = db['studlist']
```

---

# 11. Inserting Single Document

```python id="k0v8oo"
data = {
    "name":"Akhil",
    "course":"MCA",
    "mark":95
}

col.insert_one(data)
```

---

# 12. Inserting Multiple Documents

```python id="6z9m6w"
data = [
    {"name":"Akhil","mark":95},
    {"name":"Vishnu","mark":88}
]

col.insert_many(data)
```

---

# 13. Reading JSON File

```python id="1x18zr"
import json

with open("data.json") as file:
    data = json.load(file)

col.insert_many(data)
```

---

# 14. Finding Documents

## find()

Returns multiple documents.

```python id="1p0x94"
x = col.find()

for i in x:
    print(i)
```

---

## find_one()

Returns first matching document.

```python id="4oexgr"
x = col.find_one()

print(x)
```

---

# 15. Filtering Documents

```python id="4rpp4r"
x = col.find({"course":"MCA"})
```

---

# 16. Projection

Projection selects specific fields.

```python id="mzqqqo"
x = col.find({}, {"name":1, "mark":1})
```

---

# 17. Sorting Documents

```python id="rr7z7y"
x = col.find().sort("mark",-1)
```

| Value | Meaning    |
| ----- | ---------- |
| 1     | Ascending  |
| -1    | Descending |

---

# 18. Limiting Documents

```python id="y4y5e4"
x = col.find().limit(3)
```

---

# 19. Updating Single Document

```python id="3g1r85"
col.update_one(
    {"name":"Akhil"},
    {"$set":{"mark":99}}
)
```

---

# 20. Updating Multiple Documents

```python id="m1r6qo"
col.update_many(
    {},
    {"$inc":{"mark":1}}
)
```

---

# 21. Deleting Single Document

```python id="y3q7rj"
col.delete_one({"name":"Akhil"})
```

---

# 22. Deleting Multiple Documents

```python id="z7mrzz"
col.delete_many({"course":"MCA"})
```

---

# 23. MongoDB Query Operators

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `$eq`    | Equal                 |
| `$ne`    | Not equal             |
| `$gt`    | Greater than          |
| `$gte`   | Greater than or equal |
| `$lt`    | Less than             |
| `$lte`   | Less than or equal    |
| `$in`    | Match values in array |
| `$nin`   | Not in array          |

---

# 24. Query Operator Examples

## Greater Than

```python id="8mrjp6"
x = col.find({"mark":{"$gt":90}})
```

---

## Less Than

```python id="0on1zl"
x = col.find({"mark":{"$lt":50}})
```

---

## Between Two Values

```python id="m5o3jd"
x = col.find({"mark":{"$gt":80,"$lt":90}})
```

---

## Using $in

```python id="k8nd08"
x = col.find({"city":{"$in":["Kollam","Thrissur"]}})
```

---

## Using $nin

```python id="8l0dvy"
x = col.find({"city":{"$nin":["Kollam","TVM"]}})
```

---

# 25. Logical Operators

| Operator | Meaning                |
| -------- | ---------------------- |
| `$and`   | Both conditions true   |
| `$or`    | Either condition true  |
| `$not`   | Negates condition      |
| `$nor`   | Neither condition true |

---

## Example: $and

```python id="4r9xj3"
x = col.find({
    "$and":[
        {"course":"MCA"},
        {"mark":{"$gt":90}}
    ]
})
```

---

## Example: $or

```python id="mq9y6r"
x = col.find({
    "$or":[
        {"city":"Kollam"},
        {"city":"Thrissur"}
    ]
})
```

---

# 26. Regular Expressions

```python id="r7w8pj"
x = col.find({"name":{"$regex":"^A"}})
```

Matches names starting with A.

---

# 27. MongoDB Update Operators

| Operator  | Meaning                |
| --------- | ---------------------- |
| `$set`    | Set field value        |
| `$inc`    | Increment value        |
| `$rename` | Rename field           |
| `$unset`  | Remove field           |
| `$push`   | Add item to array      |
| `$pull`   | Remove item from array |

---

## Example: $set

```python id="w12m0g"
col.update_one(
    {"name":"Akhil"},
    {"$set":{"mark":100}}
)
```

---

## Example: $inc

```python id="r2vw3l"
col.update_one(
    {"name":"Akhil"},
    {"$inc":{"mark":1}}
)
```

---

# 28. Aggregation in MongoDB

Aggregation performs advanced data processing.

---

# 29. Aggregation Syntax

```python id="vxg8el"
x = col.aggregate([
    {"$match":{"course":"MCA"}},
    {"$count":"total"}
])

for i in x:
    print(i)
```

---

# 30. Aggregation Operators

| Operator   | Purpose          |
| ---------- | ---------------- |
| `$match`   | Filter documents |
| `$group`   | Group documents  |
| `$sort`    | Sort documents   |
| `$limit`   | Limit documents  |
| `$project` | Select fields    |
| `$count`   | Count documents  |

---

## Example: $sort

```python id="57yz0w"
x = col.aggregate([
    {"$sort":{"mark":-1}}
])

for i in x:
    print(i)
```

---

## Example: $limit

```python id="mjlwmx"
x = col.aggregate([
    {"$limit":3}
])

for i in x:
    print(i)
```

---

## Example: $count

```python id="gy5ox7"
x = col.aggregate([
    {"$match":{"course":"MCA"}},
    {"$count":"totalMCA"}
])

for i in x:
    print(i)
```

---

# 31. Internal Working of PyMongo

1. Python connects to MongoDB server
2. MongoClient creates connection
3. Database object is selected
4. Collection object is created
5. Documents are inserted or queried
6. MongoDB processes BSON internally
7. Results are returned to Python

---

# 32. Advantages of MongoDB

* Flexible schema
* Faster development
* Scalable architecture
* High performance
* JSON-like structure
* Easy integration with Python

---

# 33. Limitations of MongoDB

* High memory usage
* Complex joins are difficult
* Data duplication possible
* Less strict relationships

---

# 34. Applications of MongoDB

* E-commerce websites
* Social media platforms
* IoT systems
* Big data systems
* Real-time analytics
* Cloud applications

---

# 35. Common Errors

| Error             | Cause                      |
| ----------------- | -------------------------- |
| Connection Error  | MongoDB server not running |
| FileNotFoundError | Missing JSON file          |
| JSONDecodeError   | Invalid JSON               |
| DuplicateKeyError | Duplicate `_id`            |
| KeyError          | Missing field              |

---

# 36. Time Complexity

| Operation | Complexity  |
| --------- | ----------- |
| Insert    | O(1)        |
| Search    | O(n)        |
| Sort      | O(n \log n) |

Where:

* `n` = number of documents

---

# 37. Space Complexity

O(n)

---

# 38. Viva Questions and Answers

## 1. What is MongoDB?

MongoDB is a NoSQL document-oriented database that stores data in BSON format.

---

## 2. What is NoSQL?

NoSQL means non-relational database systems designed for flexible and scalable data storage.

---

## 3. What is BSON?

BSON stands for Binary JSON used internally by MongoDB.

---

## 4. Difference between SQL and MongoDB?

| SQL          | MongoDB         |
| ------------ | --------------- |
| Relational   | NoSQL           |
| Tables       | Collections     |
| Rows         | Documents       |
| Fixed schema | Flexible schema |

---

## 5. What is a collection?

A collection is a group of MongoDB documents.

---

## 6. What is a document?

A document is a JSON-like record stored in MongoDB.

---

## 7. What is PyMongo?

PyMongo is the official Python driver for MongoDB.

---

## 8. What is MongoClient?

MongoClient is the PyMongo class used to connect Python with MongoDB server.

---

## 9. Difference between find() and find_one()?

| find()                     | find_one()              |
| -------------------------- | ----------------------- |
| Returns multiple documents | Returns single document |

---

## 10. What is projection?

Projection selects specific fields from documents.

---

## 11. Explain `$gt`.

`$gt` means greater than.

Example:

```python id="7l7j6r"
{"mark":{"$gt":90}}
```

---

## 12. Explain `$in`.

`$in` checks whether a value exists in a given list.

---

## 13. Explain `$regex`.

`$regex` performs pattern matching.

---

## 14. What is aggregation?

Aggregation performs advanced data analysis and processing.

---

## 15. Explain `$match`.

`$match` filters documents during aggregation.

---

## 16. Explain `$group`.

`$group` groups documents based on specified fields.

---

## 17. Explain `$sort`.

`$sort` sorts documents in ascending or descending order.

---

## 18. Explain `$limit`.

`$limit` limits the number of documents returned.

---

## 19. Explain `$count`.

`$count` counts the number of documents.

---

## 20. Difference between insert_one() and insert_many()?

| insert_one()         | insert_many()              |
| -------------------- | -------------------------- |
| Inserts one document | Inserts multiple documents |

---

# 39. Conclusion

Thus the concepts of MongoDB and PyMongo including database creation, collection handling, CRUD operations, query operators, update operators, and aggregation functions were studied successfully using Python.
