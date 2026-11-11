# 📘 README

<div align="center">

# 🖥️ E22_StudentDatabase

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to perform student database operations.

### Operations Performed

1. View database
2. View specific record
3. Add record
4. Delete record

---

# 📘 Theory

A simple database can be created using a text file in Linux.

Each line in the file represents one student record.

Linux commands used:

| Command   | Purpose                |
| --------- | ---------------------- |
| `cat`     | Display database       |
| `grep`    | Search records         |
| `grep -v` | Delete records         |
| `>>`      | Append new records     |
| `case`    | Menu-driven operations |

This experiment demonstrates basic database management using shell scripting.

---

# 🧠 Algorithm

1. Start
2. Read database filename
3. Display menu options
4. Read user choice
5. Perform selected operation using `case` statement
6. If choice is:

   * View → display database
   * Search → find record using ID
   * Add → append new record
   * Delete → remove record using ID
7. Ask user whether to continue
8. Repeat until user exits
9. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

ch_cont="y"

read -p "Enter database name: " db

while [ "$ch_cont" = "y" ]
do
    echo "1. View Database"
    echo "2. View Specific Record"
    echo "3. Add Record"
    echo "4. Delete Record"
    echo "5. Exit"

    read -p "Enter choice: " ch

    case $ch in

    1)
        cat "$db"
        ;;

    2)
        read -p "Enter ID: " id
        grep "^$id " "$db"
        ;;

    3)
        read -p "Enter ID Name Course College: " rec
        echo "$rec" >> "$db"
        ;;

    4)
        read -p "Enter ID: " id
        grep -v "^$id " "$db" > temp
        mv temp "$db"
        echo "Record deleted"
        ;;

    5)
        exit
        ;;

    *)
        echo "Invalid choice"
        ;;

    esac

    read -p "Continue? (y/n): " ch_cont
done
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E22_StudentDatabase.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E22_StudentDatabase.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E22_StudentDatabase.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
1. View Database
2. View Specific Record
3. Add Record
4. Delete Record
5. Exit

Enter choice: 3

Enter ID Name Course College:
101 Akhil MCA CET
```

---

# 🔍 Explanation

| Command   | Description                |
| --------- | -------------------------- |
| `cat`     | Displays database contents |
| `grep`    | Searches matching records  |
| `grep -v` | Excludes matching record   |
| `>>`      | Appends data to file       |
| `case`    | Menu-driven selection      |
| `while`   | Repeats operations         |

---

# ✅ Advantages

* Simple database management system
* Easy menu-driven implementation
* Demonstrates file handling and searching concepts

---

# ❌ Limitations

* No advanced validation
* Suitable only for small text-based databases

---

# 📚 Viva Questions

## 1️⃣ What is the purpose of `grep`?

It searches matching patterns in files.

---

## 2️⃣ What does `grep -v` do?

It excludes matching lines from output.

---

## 3️⃣ What is the use of `>>` operator?

It appends data to a file.

---

## 4️⃣ Why is `case` statement used?

It is used for menu-driven selection.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to perform student database operations was executed successfully.
