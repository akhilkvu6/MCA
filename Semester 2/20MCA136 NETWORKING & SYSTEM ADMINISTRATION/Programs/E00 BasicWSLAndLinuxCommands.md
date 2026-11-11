```text id="x7m2qp"
E00_BasicWSLAndLinuxCommands.md
```

# 📘 README

<div align="center">

# 🖥️ E00_BasicWSLAndLinuxCommands

### NSA Lab – Basic WSL and Linux Commands

</div>

---

# 🎯 Aim

To study and practice basic Linux and WSL terminal commands used for file handling, navigation, permissions, execution, process management, networking, and system administration.

---

# 📘 Introduction

Windows Subsystem for Linux (WSL) allows Linux distributions to run directly on Windows systems without using a virtual machine.

Linux commands are executed through the terminal and are essential for:

* system administration
* shell scripting
* networking
* cybersecurity
* server management
* software development

This experiment demonstrates commonly used Linux terminal commands required for NSA lab practicals.

---

# 🧠 What is WSL?

WSL (Windows Subsystem for Linux) is a compatibility layer developed by Microsoft to run Linux environments directly on Windows.

## 📌 Features of WSL

* Run Linux commands on Windows
* Install Linux distributions like Ubuntu
* Execute shell scripts
* Use Linux tools and utilities
* Develop and test applications

---

# 📂 1. Navigation Commands

Navigation commands help move between directories and display current locations.

---

## 📌 Display Current Directory

```bash id="m4x8qp"
pwd
```

### 🔍 Explanation

Displays the current working directory.

---

## 📌 List Files and Directories

```bash id="v7n2zk"
ls
```

### 🔍 Explanation

Displays files and folders in current directory.

---

## 📌 Detailed File Listing

```bash id="q9p1wr"
ls -l
```

### 🔍 Explanation

Displays:

* permissions
* owner
* size
* date
* filename

---

## 📌 Change Directory

```bash id="x5m2vq"
cd foldername
```

### 🔍 Explanation

Moves into specified folder.

---

## 📌 Move Back One Directory

```bash id="k3v8zp"
cd ..
```

### 🔍 Explanation

Moves to parent directory.

---

## 📌 Go to Home Directory

```bash id="p7n1wr"
cd ~
```

### 🔍 Explanation

Moves to user's home directory.

---

# 📄 2. File Creation Commands

Commands used to create files and directories.

---

## 📌 Create Empty File

```bash id="t4m9qx"
touch file.sh
```

### 🔍 Explanation

Creates an empty file.

---

## 📌 Create/Edit File Using Nano

```bash id="v8x2zk"
nano file.sh
```

### 🔍 Explanation

Opens nano text editor.

---

## 📌 Create Directory

```bash id="m2q7vp"
mkdir foldername
```

### 🔍 Explanation

Creates a new folder.

---

# ✏️ 3. File Editing Commands

Commands used to edit and display file contents.

---

## 📌 Open File in Nano Editor

```bash id="x9p4wr"
nano file.sh
```

---

## 📌 Display File Content

```bash id="q5n8zk"
cat file.sh
```

### 🔍 Explanation

Displays contents of file.

---

## 📌 View File Page by Page

```bash id="u4m7xp"
less file.sh
```

### 🔍 Explanation

Displays large file content page-wise.

---

# 💾 4. Nano Editor Shortcuts

| Shortcut   | Function         |
| ---------- | ---------------- |
| `Ctrl + O` | Save file        |
| `Enter`    | Confirm filename |
| `Ctrl + X` | Exit nano        |
| `Ctrl + K` | Cut line         |
| `Ctrl + U` | Paste line       |
| `Ctrl + W` | Search text      |

---

# 🔐 5. File Permission Commands

Permissions control access to files and folders.

---

## 📌 Give Execute Permission

```bash id="p8x2vq"
chmod +x file.sh
```

### 🔍 Explanation

Allows script execution.

---

## 📌 Full Permission

```bash id="v3n7zk"
chmod 777 file.sh
```

### 🔍 Explanation

Provides:

* read
* write
* execute permissions

for all users.

---

## 📌 Read/Write Permission

```bash id="m6q1wr"
chmod 644 file.sh
```

### 🔍 Explanation

Owner gets read/write access while others get read-only access.

---

# ▶️ 6. Run Script Commands

Commands used to execute shell scripts.

---

## 📌 Execute Script

```bash id="x2v8qp"
./file.sh
```

---

## 📌 Execute Using Bash

```bash id="k7m4zx"
bash file.sh
```

---

# 🗑️ 7. Delete Commands

Commands used to remove files and directories.

---

## 📌 Delete File

```bash id="q3x9vp"
rm file.sh
```

---

## 📌 Delete Empty Directory

```bash id="v5m2qw"
rmdir foldername
```

---

## 📌 Delete Directory Recursively

```bash id="p4x7zn"
rm -r foldername
```

---

# 📋 8. Copy and Move Commands

Commands used for copying and renaming files.

---

## 📌 Copy File

```bash id="t9m1qp"
cp file1.sh file2.sh
```

---

## 📌 Rename/Move File

```bash id="x6v3wr"
mv old.sh new.sh
```

---

# 🔍 9. Search Commands

Commands used for searching files and text.

---

## 📌 Find File

```bash id="m8q2vx"
find . -name "file.sh"
```

---

## 📌 Search Text in File

```bash id="v4x7zp"
grep "hello" file.sh
```

---

# 👤 10. User and System Commands

Commands related to users and system information.

---

## 📌 Current User

```bash id="q1m8wr"
whoami
```

---

## 📌 Logged-in Users

```bash id="x5q2vp"
who
```

---

## 📌 Current Date and Time

```bash id="m9v4zk"
date
```

---

## 📌 System Information

```bash id="p7x1wr"
uname -a
```

---

# ⚙️ 11. Process Commands

Commands used to monitor running processes.

---

## 📌 Display Running Processes

```bash id="x7m2qp"
ps
```

---

## 📌 Live Process Monitor

```bash id="v4n8zk"
top
```

---

# 🌐 12. Networking Commands

Commands used for network-related operations.

---

## 📌 Display IP Address

```bash id="m4x8qp"
ip a
```

---

## 📌 Ping Website

```bash id="v7n2zk"
ping google.com
```

---

# 🚪 13. Exit Commands

Commands used to terminate sessions.

---

## 📌 Exit Terminal

```bash id="q9p1wr"
exit
```

---

# 🧠 Typical NSA Lab Workflow

Example workflow for shell scripting in WSL/Linux:

```bash id="x5m2vq"
cd Desktop

mkdir NSA

cd NSA

nano program.sh

chmod +x program.sh

./program.sh
```

---

# 📂 Linux File Structure Basics

| Directory | Purpose             |
| --------- | ------------------- |
| `/home`   | User files          |
| `/etc`    | Configuration files |
| `/bin`    | System commands     |
| `/var`    | Variable data       |
| `/tmp`    | Temporary files     |

---

# 🔍 Important Symbols in Linux

| Symbol | Meaning           |
| ------ | ----------------- |
| `.`    | Current directory |
| `..`   | Parent directory  |
| `~`    | Home directory    |
| `/`    | Root directory    |
| `*`    | Wildcard          |

---

# ✅ Advantages

* Easy command-line management
* Useful for scripting and automation
* Essential for system administration
* Helps learn Linux environment
* Required for networking and cybersecurity

---

# ❌ Limitations

* Requires command knowledge
* Mistyped commands may affect files
* Permission issues may occur

---

# 📚 Viva Questions

## 1️⃣ What is WSL?

WSL is Windows Subsystem for Linux.

---

## 2️⃣ What does `pwd` command do?

Displays current working directory.

---

## 3️⃣ What is the use of `chmod`?

Changes file permissions.

---

## 4️⃣ What is `nano`?

Nano is a terminal-based text editor.

---

## 5️⃣ Difference between `cp` and `mv`?

`cp` copies files while `mv` moves or renames files.

---

## 6️⃣ What does `ls -l` display?

Detailed file information.

---

## 7️⃣ What is shell scripting?

Writing Linux commands in a file to automate tasks.

---

## 8️⃣ What is the use of `grep`?

Searches text patterns.

---

## 9️⃣ What does `top` command do?

Displays running processes live.

---

## 🔟 What is the purpose of `chmod +x`?

Gives execute permission to file.

---

# 🎓 Result

Thus, the basic WSL and Linux terminal commands for navigation, file handling, permissions, execution, networking, and process management were studied and executed successfully.
