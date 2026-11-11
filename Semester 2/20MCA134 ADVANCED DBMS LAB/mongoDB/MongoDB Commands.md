<div align="center">

# MONGODB COMMANDS GUIDE
## Advanced DBMS Lab - MCA Semester 2

</div>

---

# Introduction

MongoDB is a NoSQL database that stores data in the form of:
- collections
- documents

MongoDB stores data using:
```json
JSON-like BSON documents
```

Unlike MySQL:
- MongoDB is schema-less
- does not use tables and rows

---

# MongoDB Terminology

| SQL | MongoDB |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key | `_id` |
| Join | Embedded Documents |

---

# MongoDB File Extensions

| Extension | Purpose |
|---|---|
| `.js` | MongoDB Shell Scripts |
| `.md` | Documentation |

---

# Starting MongoDB

## Start MongoDB Server

```bash
mongod
```

---

# Open MongoDB Shell

```bash
mongosh
```

---

# Show All Databases

```javascript
show dbs
```

---

# Create / Switch Database

```javascript
use studentDB
```

If database does not exist:
- MongoDB creates it automatically when data is inserted.

---

# Check Current Database

```javascript
db
```

---

# Create Collection

```javascript
db.createCollection("student")
```

---

# Show Collections

```javascript
show collections
```

---

# Insert One Document

```javascript
db.student.insertOne(
{
    name: "Akhil",
    age: 22,
    course: "MCA"
}
)
```

---

# Insert Multiple Documents

```javascript
db.student.insertMany(
[
    {
        name: "Akhil",
        age: 22,
        course: "MCA"
    },

    {
        name: "Rahul",
        age: 23,
        course: "MCA"
    }
]
)
```

---

# View All Documents

```javascript
db.student.find()
```

---

# Pretty Print Documents

```javascript
db.student.find().pretty()
```

---

# Find One Document

```javascript
db.student.findOne()
```

---

# Find Using Condition

```javascript
db.student.find(
{
    age: 22
}
)
```

---

# Comparison Operators

| Operator | Meaning |
|---|---|
| `$gt` | Greater Than |
| `$lt` | Less Than |
| `$gte` | Greater Than or Equal |
| `$lte` | Less Than or Equal |
| `$eq` | Equal |
| `$ne` | Not Equal |

---

# Example - Greater Than

```javascript
db.student.find(
{
    age:
    {
        $gt: 20
    }
}
)
```

---

# Logical Operators

| Operator | Meaning |
|---|---|
| `$and` | AND |
| `$or` | OR |
| `$not` | NOT |

---

# Example - AND Condition

```javascript
db.student.find(
{
    $and:
    [
        { age: 22 },
        { course: "MCA" }
    ]
}
)
```

---

# Update One Document

```javascript
db.student.updateOne(
{
    name: "Akhil"
},
{
    $set:
    {
        age: 23
    }
}
)
```

---

# Update Multiple Documents

```javascript
db.student.updateMany(
{},
{
    $set:
    {
        status: "Active"
    }
}
)
```

---

# Replace Entire Document

```javascript
db.student.replaceOne(
{
    name: "Akhil"
},
{
    name: "Akhil",
    age: 24,
    course: "MCA"
}
)
```

---

# Delete One Document

```javascript
db.student.deleteOne(
{
    name: "Rahul"
}
)
```

---

# Delete Multiple Documents

```javascript
db.student.deleteMany(
{
    age:
    {
        $lt: 20
    }
}
)
```

---

# Delete All Documents

```javascript
db.student.deleteMany({})
```

---

# Drop Collection

```javascript
db.student.drop()
```

---

# Drop Database

```javascript
db.dropDatabase()
```

---

# Sorting Documents

## Ascending Order

```javascript
db.student.find().sort(
{
    age: 1
}
)
```

---

## Descending Order

```javascript
db.student.find().sort(
{
    age: -1
}
)
```

---

# Limit Documents

```javascript
db.student.find().limit(2)
```

---

# Skip Documents

```javascript
db.student.find().skip(2)
```

---

# Count Documents

```javascript
db.student.countDocuments()
```

---

# Create Index

```javascript
db.student.createIndex(
{
    name: 1
}
)
```

---

# View Indexes

```javascript
db.student.getIndexes()
```

---

# Embedded Documents

```javascript
db.student.insertOne(
{
    name: "Akhil",

    address:
    {
        city: "Thrissur",
        state: "Kerala"
    }
}
)
```

---

# Array Field Example

```javascript
db.student.insertOne(
{
    name: "Akhil",

    skills:
    [
        "Java",
        "MongoDB",
        "Python"
    ]
}
)
```

---

# Aggregation

## Group Example

```javascript
db.student.aggregate(
[
    {
        $group:
        {
            _id: "$course",
            total:
            {
                $sum: 1
            }
        }
    }
]
)
```

---

# Backup Database

```bash
mongodump
```

---

# Restore Database

```bash
mongorestore
```

---

# Import JSON File

```bash
mongoimport --db studentDB --collection student --file student.json --jsonArray
```

---

# Export Collection

```bash
mongoexport --db studentDB --collection student --out student.json
```

---

# MongoDB Compass

MongoDB Compass is GUI tool for MongoDB.

Features:
- View documents
- Insert data
- Delete data
- Run queries
- Aggregation pipeline

---

# Common Errors

## 1. mongosh not recognized

### Reason

MongoDB path not added to environment variables.

### Solution

Add MongoDB bin folder to PATH.

Example:

```text
C:\Program Files\MongoDB\Server\8.0\bin
```

---

# 2. Failed to connect to localhost

### Reason

MongoDB service not running.

### Solution

Start MongoDB service.

---

# 3. Unauthorized Error

### Reason

Authentication enabled.

### Solution

Use:
```bash
mongosh -u username -p password
```

---

# Advantages of MongoDB

- Schema-less
- Flexible
- High Performance
- Scalable
- JSON-like Documents
- Easy Replication

---

# Disadvantages of MongoDB

- No complex joins like SQL
- High memory usage
- Less strict schema validation

---

# SQL vs MongoDB

| SQL | MongoDB |
|---|---|
| Table | Collection |
| Row | Document |
| Fixed Schema | Dynamic Schema |
| Relational | Non-Relational |
| SQL Queries | JSON Queries |

---

# Frequently Used MongoDB Commands

| Command | Purpose |
|---|---|
| `show dbs` | Show databases |
| `use dbname` | Switch database |
| `show collections` | Show collections |
| `db.collection.find()` | View documents |
| `insertOne()` | Insert document |
| `updateOne()` | Update document |
| `deleteOne()` | Delete document |
| `drop()` | Delete collection |

---

# Viva Questions

## Q1. What is MongoDB?
MongoDB is a NoSQL document-oriented database.

---

## Q2. What is a collection?
Collection is similar to table in SQL.

---

## Q3. What is a document?
Document is similar to row in SQL.

---

## Q4. What is BSON?
Binary form of JSON used internally by MongoDB.

---

## Q5. What is `_id` field?
Unique identifier for each document.

---

## Q6. Difference between SQL and MongoDB?

| SQL | MongoDB |
|---|---|
| Relational | Non-Relational |
| Tables | Collections |
| Rows | Documents |

---

## Q7. What is aggregation?
Process of data analysis and grouping.

---

## Q8. What is schema-less database?
Database without fixed structure.

---

## Q9. What is MongoDB Compass?
GUI tool for MongoDB.

---

## Q10. How to show all databases?

```javascript
show dbs
```

---

<div align="center">

# MongoDB Quick Reference Guide

Useful for:
- DBMS Lab
- MongoDB Practicals
- Viva Preparation
- Project Development

</div>