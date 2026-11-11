# 📘 README

<div align="center">

# 🖥️ E06_NumberOfTerminalsLogged

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to find the number of terminals a user is logged into.

---

# 📘 Theory

In Linux, the `who` command displays the list of users currently logged into the system.

The `grep -c` command is used to count the number of occurrences of a username.

This experiment:

* accepts username as command-line argument
* stores logged-in user details in a file
* counts how many times the username appears

### Concepts Used

* Shell scripting
* Command-line arguments
* File handling
* `who` command
* `grep` command

---

# 🧠 Algorithm

1. Start
2. Check whether one command-line argument is provided
3. If argument exists
4. Store logged-in users using `who` command
5. Count occurrences of username using `grep -c`
6. Display number of terminals logged in
7. Otherwise display error message
8. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

if [ $# -eq 1 ]
then
    who > users.txt

    echo "$1 user is logged in:"

    grep -c "$1" users.txt
else
    echo "Please enter username"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E06_NumberOfTerminalsLogged.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E06_NumberOfTerminalsLogged.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E06_NumberOfTerminalsLogged.sh akhil
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
akhil user is logged in:
2
```

---

# 🔍 Explanation

| Symbol / Command | Description                      |
| ---------------- | -------------------------------- |
| `$#`             | Number of command-line arguments |
| `$1`             | First command-line argument      |
| `who`            | Displays logged-in users         |
| `>`              | Redirects output to file         |
| `grep -c`        | Counts matching occurrences      |
| `if`             | Conditional statement            |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates user monitoring in Linux
* Useful for learning command-line arguments

---

# ❌ Limitations

* Creates temporary file unnecessarily
* Depends on logged-in users availability

---

# 📚 Viva Questions

## 1️⃣ What does `who` command do?

It displays currently logged-in users.

---

## 2️⃣ What is the purpose of `grep -c`?

It counts matching occurrences.

---

## 3️⃣ What does `$1` represent?

It represents the first command-line argument.

---

## 4️⃣ What is the use of `$#`?

It stores the number of command-line arguments.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to find the number of terminals a user is logged into was executed successfully.
