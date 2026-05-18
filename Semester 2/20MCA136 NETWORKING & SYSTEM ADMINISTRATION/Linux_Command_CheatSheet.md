```text id="x7m2qp"
Linux_Command_CheatSheet.md
```

# 📘 Linux Command Cheat Sheet

<div align="center">

# 🐧 Linux & WSL Command Cheat Sheet

### NSA Lab Reference Guide

</div>

---

# 📂 1. Navigation Commands

| Command     | Description                     |
| ----------- | ------------------------------- |
| `pwd`       | Print current working directory |
| `ls`        | List files and folders          |
| `ls -l`     | Detailed file listing           |
| `ls -a`     | Show hidden files               |
| `cd folder` | Change directory                |
| `cd ..`     | Move to parent directory        |
| `cd ~`      | Go to home directory            |

---

# 📄 2. File Commands

| Command              | Description           |
| -------------------- | --------------------- |
| `touch file.txt`     | Create empty file     |
| `cat file.txt`       | Display file contents |
| `nano file.txt`      | Open file editor      |
| `cp a.txt b.txt`     | Copy file             |
| `mv old.txt new.txt` | Rename/move file      |
| `rm file.txt`        | Delete file           |
| `mkdir folder`       | Create folder         |
| `rmdir folder`       | Remove empty folder   |

---

# 🔐 3. Permission Commands

| Command            | Description             |
| ------------------ | ----------------------- |
| `chmod +x file.sh` | Give execute permission |
| `chmod 777 file`   | Full permission         |
| `chmod 644 file`   | Read/write for owner    |
| `chown user file`  | Change owner            |

---

# ▶️ 4. Script Execution

| Command        | Description           |
| -------------- | --------------------- |
| `./file.sh`    | Execute script        |
| `bash file.sh` | Run script using bash |

---

# 🔍 5. Search Commands

| Command                 | Description         |
| ----------------------- | ------------------- |
| `find . -name "a.txt"`  | Search file         |
| `grep "hello" file.txt` | Search text         |
| `locate file.txt`       | Locate file quickly |

---

# ⚙️ 6. Process Commands

| Command    | Description           |
| ---------- | --------------------- |
| `ps`       | Show processes        |
| `ps aux`   | Detailed process list |
| `top`      | Live process monitor  |
| `kill PID` | Stop process          |

---

# 🌐 7. Networking Commands

| Command                 | Description        |
| ----------------------- | ------------------ |
| `ip a`                  | Show IP address    |
| `ping google.com`       | Test connectivity  |
| `ssh user@ip`           | Remote login       |
| `scp file user@ip:path` | Copy file remotely |

---

# 👤 8. User Commands

| Command        | Description      |
| -------------- | ---------------- |
| `whoami`       | Current username |
| `who`          | Logged-in users  |
| `passwd`       | Change password  |
| `useradd name` | Add user         |
| `userdel name` | Delete user      |

---

# 📊 9. System Commands

| Command    | Description        |
| ---------- | ------------------ |
| `uname -a` | System information |
| `date`     | Current date/time  |
| `cal`      | Calendar           |
| `history`  | Command history    |

---

# 🧠 10. Common Linux Symbols

| Symbol | Meaning           |             |
| ------ | ----------------- | ----------- |
| `.`    | Current directory |             |
| `..`   | Parent directory  |             |
| `~`    | Home directory    |             |
| `/`    | Root directory    |             |
| `*`    | Wildcard          |             |
| `>`    | Redirect output   |             |
| `>>`   | Append output     |             |
| `      | `                 | Pipe output |

---

# 🔥 11. Important Command Options

---

# 📌 `echo` Command Options

## 🔹 `-n`

```bash id="m4x8qp"
echo -n "Hello"
```

### Purpose

Prevents newline after output.

### Output

```text id="v7n2zk"
Hello
```

Cursor remains on same line.

---

# 📌 `read` Command Options

---

## 🔹 `-p`

```bash id="q9p1wr"
read -p "Enter Name: " name
```

### Purpose

Displays prompt message while taking input.

---

## 🔹 `-s`

```bash id="x5m2vq"
read -s password
```

### Purpose

Hides typed input.

Used for passwords.

---

## 🔹 `-n`

```bash id="k3v8zp"
read -n 1 ch
```

### Purpose

Reads only specified number of characters.

---

## 🔹 `-t`

```bash id="p7n1wr"
read -t 5 input
```

### Purpose

Waits for input only for specified seconds.

---

# 📌 `ls` Command Options

---

## 🔹 `-l`

```bash id="t4m9qx"
ls -l
```

### Purpose

Displays detailed listing.

Shows:

* permissions
* owner
* size
* date

---

## 🔹 `-a`

```bash id="v8x2zk"
ls -a
```

### Purpose

Shows hidden files.

---

## 🔹 `-h`

```bash id="m2q7vp"
ls -lh
```

### Purpose

Displays file size in human-readable format.

Example:

```text id="x9p4wr"
2K
5M
1G
```

---

# 📌 `rm` Command Options

---

## 🔹 `-r`

```bash id="q5n8zk"
rm -r folder
```

### Purpose

Deletes directory recursively.

---

## 🔹 `-f`

```bash id="u4m7xp"
rm -f file.txt
```

### Purpose

Force delete without confirmation.

---

# 📌 `cp` Command Options

---

## 🔹 `-r`

```bash id="p8x2vq"
cp -r folder1 folder2
```

### Purpose

Copies directories recursively.

---

# 📌 `mkdir` Command Options

---

## 🔹 `-p`

```bash id="v3n7zk"
mkdir -p a/b/c
```

### Purpose

Creates parent directories automatically.

---

# 📌 `grep` Command Options

---

## 🔹 `-i`

```bash id="m6q1wr"
grep -i hello file.txt
```

### Purpose

Ignores case sensitivity.

---

## 🔹 `-n`

```bash id="x2v8qp"
grep -n hello file.txt
```

### Purpose

Displays line numbers.

---

## 🔹 `-c`

```bash id="k7m4zx"
grep -c hello file.txt
```

### Purpose

Counts matching lines.

---

# 📌 `find` Command Options

---

## 🔹 `-name`

```bash id="q3x9vp"
find . -name "file.txt"
```

### Purpose

Search by filename.

---

## 🔹 `-type`

```bash id="v5m2qw"
find . -type d
```

### Purpose

Search by type.

| Type | Meaning   |
| ---- | --------- |
| `f`  | File      |
| `d`  | Directory |

---

# 📌 `chmod` Permission Numbers

| Number | Permission             |
| ------ | ---------------------- |
| 7      | Read + Write + Execute |
| 6      | Read + Write           |
| 5      | Read + Execute         |
| 4      | Read only              |

Example:

```bash id="p4x7zn"
chmod 755 file.sh
```

---

# 📌 `head` and `tail`

---

## 🔹 `head -n`

```bash id="t9m1qp"
head -n 5 file.txt
```

### Purpose

Shows first 5 lines.

---

## 🔹 `tail -n`

```bash id="x6v3wr"
tail -n 5 file.txt
```

### Purpose

Shows last 5 lines.

---

# 📌 `wc` Command Options

| Option | Purpose          |
| ------ | ---------------- |
| `-l`   | Count lines      |
| `-w`   | Count words      |
| `-c`   | Count characters |

Example:

```bash id="m8q2vx"
wc -l file.txt
```

---

# 📌 `tar` Compression Commands

## Create Archive

```bash id="v4x7zp"
tar -cvf backup.tar folder
```

---

## Extract Archive

```bash id="q1m8wr"
tar -xvf backup.tar
```

---

# 📌 Redirection Operators

---

## 🔹 `>`

```bash id="x5q2vp"
echo "Hello" > file.txt
```

### Purpose

Overwrite file.

---

## 🔹 `>>`

```bash id="m9v4zk"
echo "World" >> file.txt
```

### Purpose

Append to file.

---

# 📌 Pipe Operator

```bash id="p7x1wr"
ls | wc -l
```

### Purpose

Pass output of one command to another.

---

# 🧪 Common NSA Lab Workflow

```bash id="x7m2qp"
mkdir NSA

cd NSA

nano program.sh

chmod +x program.sh

./program.sh
```

---

# 📚 Useful Linux Shortcuts

| Shortcut   | Function          |
| ---------- | ----------------- |
| `Ctrl + C` | Stop process      |
| `Ctrl + Z` | Suspend process   |
| `Ctrl + L` | Clear screen      |
| `Ctrl + A` | Beginning of line |
| `Ctrl + E` | End of line       |

---

# ✅ Advantages of Linux Commands

* Fast system management
* Automation support
* Powerful scripting
* Remote administration
* Essential for networking

---

# 🎓 Result

Thus, various Linux and WSL terminal commands, options, permissions, networking commands, process commands, and scripting-related operations were studied successfully.
