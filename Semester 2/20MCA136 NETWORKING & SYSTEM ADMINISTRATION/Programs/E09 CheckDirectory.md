# 📘 README

<div align="center">

# 🖥️ E09_CheckDirectory

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to check whether a file is a directory or not.

---

# 📘 Theory

In Linux, directories are special types of files used to store other files and folders.

The `-d` file test operator is used to check whether a given path is a directory.

Syntax:

```text id="m4x8vq"
[ -d directory_name ]
```

If the specified path exists and is a directory, the condition becomes true.

### Concepts Used

* Shell scripting
* File test operators
* Conditional statements
* For loop

---

# 🧠 Algorithm

1. Start
2. Read directory name from the user
3. Store the directory path
4. Check whether the given path is a directory using `-d`
5. If true, display directory exists message
6. Otherwise display not a directory message
7. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

read -p "Enter directory name you want to search: " dir

for filename in "E:/MCA/S2/lab/$dir"
do
    if [ -d "$filename" ]
    then
        echo "$filename is a directory"
    else
        echo "$filename is not directory"
    fi
done
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E09_CheckDirectory.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E09_CheckDirectory.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E09_CheckDirectory.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Enter directory name you want to search: Programs

E:/MCA/S2/lab/Programs is a directory
```

---

# 🔍 Explanation

| Symbol / Command | Description                        |
| ---------------- | ---------------------------------- |
| `read -p`        | Accepts input with prompt          |
| `for`            | Loop statement                     |
| `-d`             | Checks whether path is a directory |
| `if`             | Conditional statement              |
| `echo`           | Displays output                    |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates directory checking in shell scripting
* Useful for file system operations

---

# ❌ Limitations

* Uses fixed directory path
* Depends on valid path availability

---

# 📚 Viva Questions

## 1️⃣ What does `-d` operator do?

It checks whether a file path is a directory.

---

## 2️⃣ What is a directory?

A directory is a container used to store files and folders.

---

## 3️⃣ What is the purpose of `read -p`?

It displays a prompt and accepts user input.

---

## 4️⃣ Why is `if` statement used?

It is used for decision making based on conditions.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to check whether a file is a directory or not was executed successfully.
