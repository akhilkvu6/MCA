# 📘 README

<div align="center">

# 🖥️ E14_SystemConfig

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to display system configuration details.

---

# 📘 Theory

Linux provides several environment variables and commands to display system configuration and hardware details.

This experiment uses:

* environment variables
* Linux system commands
* shell scripting

to display important system information such as:

* current shell
* home directory
* operating system type
* current user
* hostname
* kernel version
* memory and disk information

---

# 🧠 Algorithm

1. Start
2. Display current shell using `$SHELL`
3. Display home directory using `$HOME`
4. Display operating system type using `$OSTYPE`
5. Display current working directory using `pwd`
6. Display current username using `whoami`
7. Display hostname using `hostname`
8. Display kernel version and architecture using `uname`
9. Display date and time using `date`
10. Display logged-in users using `who`
11. Display disk space using `df -h`
12. Display memory information using `free -h`
13. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo "===== SYSTEM CONFIGURATION ====="

echo "Current Shell: $SHELL"

echo "------------------------"

echo "Home Directory: $HOME"

echo "------------------------"

echo "Operating System Type: $OSTYPE"

echo "------------------------"

echo "Current Working Directory:"
pwd

echo "------------------------"

echo "Current User:"
whoami

echo "------------------------"

echo "Hostname:"
hostname

echo "------------------------"

echo "Kernel Version:"
uname -r

echo "------------------------"

echo "System Architecture:"
uname -m

echo "------------------------"

echo "Present Date and Time:"
date

echo "------------------------"

echo "Logged In Users:"
who

echo "------------------------"

echo "Disk Space Information:"
df -h

echo "------------------------"

echo "Memory Information:"
free -h
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E14_SystemConfig.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E14_SystemConfig.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E14_SystemConfig.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
===== SYSTEM CONFIGURATION =====

Current Shell: /bin/bash

Home Directory: /home/akhil

Operating System Type: linux-gnu

Current Working Directory:
/home/akhil

Current User:
akhil

Hostname:
FX516PC

Kernel Version:
5.15.167.4-microsoft-standard-WSL2
```

---

# 🔍 Explanation

| Variable / Command | Description                    |
| ------------------ | ------------------------------ |
| `$SHELL`           | Displays current shell         |
| `$HOME`            | Displays home directory        |
| `$OSTYPE`          | Displays OS type               |
| `pwd`              | Displays current directory     |
| `whoami`           | Displays current user          |
| `hostname`         | Displays system hostname       |
| `uname -r`         | Displays kernel version        |
| `uname -m`         | Displays system architecture   |
| `date`             | Displays current date and time |
| `who`              | Displays logged-in users       |
| `df -h`            | Displays disk space            |
| `free -h`          | Displays memory usage          |

---

# ✅ Advantages

* Displays complete system information
* Useful for system monitoring
* Demonstrates Linux environment variables and commands

---

# ❌ Limitations

* Output varies between systems
* Some commands may require permissions in restricted systems

---

# 📚 Viva Questions

## 1️⃣ What does `$SHELL` variable store?

It stores the current shell path.

---

## 2️⃣ What is the use of `pwd` command?

It displays the current working directory.

---

## 3️⃣ What does `uname -r` display?

It displays Linux kernel version.

---

## 4️⃣ What is the purpose of `df -h`?

It displays disk space usage in human-readable format.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to display system configuration details was executed successfully.
