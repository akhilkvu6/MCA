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

# 1. Display name and mark of all female students in MCA

print("\n1. Female students in MCA")

x = db.studlist.find(
    {"gender":"female","course":"MCA"},
    {"name":1,"mark":1}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'], "| Mark:", i['mark'])

# 2. Display the details of student who secured highest mark in MCA

print("\n2. Highest mark in MCA")

x = db.studlist.find(
    {"course":"MCA"}
).sort("mark",-1).limit(1)

for i in x:
    print(i)

# 3. Display all male students who scored A+ grade

print("\n3. Male students with A+ grade")

x = db.studlist.find(
    {"grade":"A+","gender":"male"}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'])

# 4. Display top 3 students in Mechanical department

print("\n4. Top 3 students in Mechanical department")

x = db.studlist.find(
    {"course":"Mechanical"}
).sort("mark",-1).limit(3)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'], "| Mark:", i['mark'])

# 5. Display female students with marks greater than 90

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

# 6. Display students with marks between 80 and 90

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

# 7. Display students whose name starts with V

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

# 8. Display all students from Kollam

print("\n8. Students from Kollam")

x = db.studlist.find(
    {"address.city":"Kollam"}
)

for i in x:
    print("Name:", i['name']['fname'], i['name']['lname'])

# 9. Display students not from Kollam or Thiruvananthapuram

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

# 10. Display female students from Kollam or Thiruvananthapuram

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