# 📘 README

<div align="center">

# 🖥️ E10_CountNumberOfFiles

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to count the number of files in a directory.

---

# 📘 Theory

In Linux, files and folders inside a directory can be counted using commands like:

* `ls` → lists directory contents
* `wc -l` → counts number of lines

When combined together:

```text id="m4x8vq"
ls directory | wc -l
```

the total number of items inside the directory is displayed.

This experiment checks whether the directory exists and then counts the files inside it.

### Concepts Used

* Shell scripting
* Directory handling
* File counting
* Conditional statements
* Linux commands

---

# 🧠 Algorithm

1. Start
2. Read directory name from the user
3. Create full directory path
4. Check whether directory exists using `-d`
5. If directory exists
6. List directory contents using `ls`
7. Count number of entries using `wc -l`
8. Display count
9. Otherwise display error message
10. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

read -p "Enter directory name you want to search: " dir

direct="E:/MCA/S2/lab/$dir"

if [ -d "$direct" ]
then
    count=$(ls "$direct" | wc -l)
    echo "Number of files in $direct = $count"
else
    echo "Directory not found"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E10_CountNumberOfFiles.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E10_CountNumberOfFiles.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E10_CountNumberOfFiles.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Enter directory name you want to search: test

Number of files in E:/MCA/S2/lab/test = 6
```

---

# 🔍 Explanation

| Symbol / Command | Description                     |
| ---------------- | ------------------------------- |
| `read -p`        | Accepts input with prompt       |
| `-d`             | Checks whether directory exists |
| `ls`             | Lists directory contents        |
| `wc -l`          | Counts number of lines/files    |
| `if`             | Conditional statement           |
| `echo`           | Displays output                 |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates directory handling in Linux
* Useful for file system operations

---

# ❌ Limitations

* Counts both files and folders
* Hidden files are not included by default

---

# 📚 Viva Questions

## 1️⃣ What does `ls` command do?

It lists files and directories.

---

## 2️⃣ What is the use of `wc -l`?

It counts the number of lines.

---

## 3️⃣ What does `-d` operator check?

It checks whether a directory exists.

---

## 4️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

## 5️⃣ Does this script count hidden files?

No, hidden files are not counted by default.

---

# 🎓 Result

Thus, the shell script to count the number of files in a directory was executed successfully.
