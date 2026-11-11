# 📘 README

<div align="center">

# 🖥️ E20_SystemInformation

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to display various system information details.

### Operations Performed

1. Count logged-in users
2. Display column list of files in home directory
3. Display below priority jobs
4. Display date and time
5. Display current working directory
6. Display system uptime
7. Display disk space information

---

# 📘 Theory

Linux provides several commands to retrieve system-related information.

This experiment uses commands such as:

* `who`
* `wc`
* `ls`
* `cut`
* `ps`
* `date`
* `pwd`
* `uptime`
* `df`

to monitor users, files, processes, and system status.

---

# 🧠 Algorithm

1. Start
2. Count logged-in users using `who | wc -l`
3. Display selected columns of files using `ls -l` and `cut`
4. Display below priority jobs using `ps -al` and `cut`
5. Display current date and time using `date`
6. Display current working directory using `pwd`
7. Display system uptime using `uptime`
8. Display disk space using `df -h`
9. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo "1. Count of users logged in:"
who | wc -l

echo "--------------------------------"

echo "2. Column list of files in home directory:"
ls -l $HOME | cut -c 17-24,39-50,56-

echo "--------------------------------"

echo "3. List of below priority jobs:"
ps -al | cut -c 16-19,70-

echo "--------------------------------"

echo "4. Current Date and Time:"
date

echo "--------------------------------"

echo "5. Current Working Directory:"
pwd

echo "--------------------------------"

echo "6. System Uptime:"
uptime

echo "--------------------------------"

echo "7. Disk Space Information:"
df -h
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E20_SystemInformation.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E20_SystemInformation.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E20_SystemInformation.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
1. Count of users logged in:
3

--------------------------------

2. Column list of files in home directory:
4096 Jan 12 file1.txt

--------------------------------

3. List of below priority jobs:
1234 bash

--------------------------------

4. Current Date and Time:
Thu May 15 10:20:35 IST 2026
```

---

# 🔍 Explanation

| Command  | Description                    |
| -------- | ------------------------------ |
| `who`    | Displays logged-in users       |
| `wc -l`  | Counts number of lines/users   |
| `ls -l`  | Lists files with details       |
| `cut`    | Extracts selected columns      |
| `ps -al` | Displays process information   |
| `date`   | Displays current date and time |
| `pwd`    | Displays current directory     |
| `uptime` | Displays system running time   |
| `df -h`  | Displays disk space usage      |

---

# ✅ Advantages

* Displays useful system information
* Demonstrates Linux monitoring commands
* Useful for system administration practice

---

# ❌ Limitations

* Output varies from system to system
* Some processes may require permissions to view fully

---

# 📚 Viva Questions

## 1️⃣ What does `who` command display?

It displays logged-in users.

---

## 2️⃣ What is the use of `wc -l`?

It counts number of lines.

---

## 3️⃣ What does `ps -al` display?

It displays process details.

---

## 4️⃣ What is the purpose of `df -h`?

It displays disk space in human-readable format.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to display various system information details was executed successfully.
