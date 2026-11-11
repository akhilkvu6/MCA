from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["exam"]
col = db["stmarks"]

while True:
    print("\n--- STUDENT SYSTEM ---")
    print("1. Add Student")
    print("2. View All")
    print("3. Search by Rollno")
    print("4. Topper")
    print("5. Count Students")
    print("6. Name starts with A")
    print("7. Marks <= 100")
    print("8. Update Total")
    print("9. Delete by Name")
    print("10. Exit")

    ch = int(input("Enter choice: "))

    # 1 Add
    if ch == 1:
        roll = int(input("Rollno: "))
        name = input("Name: ")
        m1 = int(input("Mark1: "))
        m2 = int(input("Mark2: "))
        m3 = int(input("Mark3: "))

        total = m1 + m2 + m3

        col.insert_one({
            "rollno": roll,
            "name": name,
            "mark1": m1,
            "mark2": m2,
            "mark3": m3,
            "total": total
        })

        print("✅ Inserted")

    # 2 View
    elif ch == 2:
        for doc in col.find({}, {"_id": 0}):
            print(doc)

    # 3 Search
    elif ch == 3:
        roll = int(input("Rollno: "))
        print(col.find_one({"rollno": roll}, {"_id": 0}))

    # 4 Topper
    elif ch == 4:
        top = col.find({}, {"name":1,"total":1,"_id":0}).sort("total",-1).limit(1)
        for t in top:
            print("Topper:", t)

    # 5 Count
    elif ch == 5:
        print("Total Students:", col.count_documents({}))

    # 6 Regex
    elif ch == 6:
        for i in col.find({"name":{"$regex":"^A"}},{"name":1,"_id":0}):
            print(i)

    # 7 Condition
    elif ch == 7:
        for i in col.find({"total":{"$lte":100}},{"name":1,"total":1,"_id":0}):
            print(i)

    # 8 Update
    elif ch == 8:
        roll = int(input("Rollno: "))
        new_total = int(input("New total: "))
        col.update_one({"rollno": roll},{"$set":{"total": new_total}})
        print("Updated")

    # 9 Delete
    elif ch == 9:
        name = input("Enter name: ")
        col.delete_many({"name": name})
        print("Deleted")

    # 10 Exit
    elif ch == 10:
        break

    else:
        print("Invalid choice")