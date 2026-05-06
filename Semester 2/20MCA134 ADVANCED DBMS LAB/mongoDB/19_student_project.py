from pymongo import MongoClient

# Connect
client = MongoClient("mongodb://localhost:27017")
db = client["Akhil"]
col = db["students"]

while True:
    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Add Student")
    print("2. View All")
    print("3. Search by Rollno")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    # 1. Add Student
    if choice == 1:
        roll = int(input("Enter rollno: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        col.insert_one({
            "rollno": roll,
            "name": name,
            "marks": marks
        })

        print("✅ Student added")

    # 2. View All
    elif choice == 2:
        print("\nAll Students:")
        for doc in col.find({}, {"_id": 0}):
            print(doc)

    # 3. Search
    elif choice == 3:
        roll = int(input("Enter rollno: "))
        doc = col.find_one({"rollno": roll}, {"_id": 0})

        if doc:
            print(doc)
        else:
            print("❌ Not found")

    # 4. Update
    elif choice == 4:
        roll = int(input("Enter rollno: "))
        new_marks = int(input("Enter new marks: "))

        col.update_one(
            {"rollno": roll},
            {"$set": {"marks": new_marks}}
        )

        print("✅ Updated")

    # 5. Delete
    elif choice == 5:
        roll = int(input("Enter rollno: "))

        col.delete_one({"rollno": roll})
        print("✅ Deleted")

    # 6. Exit
    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice")