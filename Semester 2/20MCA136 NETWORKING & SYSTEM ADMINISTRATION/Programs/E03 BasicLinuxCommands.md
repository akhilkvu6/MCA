# 📘 README

<div align="center">

# 🖥️ E03_BasicLinuxCommands

### NSA Lab – Basic Linux Commands

</div>

---

# 🎯 Aim

To study and execute basic Linux commands used for file handling, directory management, user management, process monitoring, and networking.

---

# 📘 Theory

Linux is an open-source operating system that provides powerful command-line utilities.

Linux commands help users to:

* manage files and directories
* monitor system processes
* manage users and permissions
* perform networking operations
* automate tasks

This experiment demonstrates commonly used Linux commands with examples.

---

# 🧪 Linux Commands and Examples

| No. | Command   | Purpose                 |
| --- | --------- | ----------------------- |
| 1   | `man`     | Display manual/help     |
| 2   | `ls`      | List files              |
| 3   | `echo`    | Print/write text        |
| 4   | `read`    | Accept user input       |
| 5   | `cat`     | Display file            |
| 6   | `cd`      | Change directory        |
| 7   | `mkdir`   | Create directory        |
| 8   | `pwd`     | Print working directory |
| 9   | `mv`      | Move/rename file        |
| 10  | `cp`      | Copy file               |
| 11  | `rm`      | Delete file             |
| 12  | `touch`   | Create empty file       |
| 13  | `chmod`   | Change permissions      |
| 14  | `chown`   | Change owner            |
| 15  | `more`    | View file page-wise     |
| 16  | `less`    | Advanced file viewer    |
| 17  | `find`    | Search files            |
| 18  | `wc`      | Count lines/words       |
| 19  | `cut`     | Extract data            |
| 20  | `paste`   | Merge files             |
| 21  | `head`    | Display first lines     |
| 22  | `tail`    | Display last lines      |
| 23  | `useradd` | Add user                |
| 24  | `userdel` | Delete user             |
| 25  | `usermod` | Modify user             |
| 26  | `passwd`  | Change password         |
| 27  | `top`     | System monitor          |
| 28  | `ps`      | Process status          |
| 29  | `ssh`     | Remote login            |
| 30  | `scp`     | Secure copy             |

---

# 🧠 Algorithm

1. Start
2. Execute Linux commands one by one
3. Observe their outputs
4. Understand file handling, user management, process management, and networking operations
5. Stop

---

# 💻 Program

```bash id="m4x8qp"
#!/bin/bash

echo "===== BASIC LINUX COMMANDS ====="

echo "1. man – manual/help"
echo "Shows full documentation of a command"
echo "Command: man ls"

echo "------------------------"

echo "2. ls – list files"
ls -l

echo "------------------------"

echo "3. echo – print/write text"
echo "Hello World"
echo "Hello" > file.txt

echo "------------------------"

echo "4. read – take input"
read -p "Enter your name: " name
echo "$name"

echo "------------------------"

echo "5. cat – display file"
cat file.txt

echo "------------------------"

echo "6. cd – change directory"
echo "Command: cd /home/user/Documents"

echo "------------------------"

echo "7. mkdir – create directory"
mkdir myfolder

echo "------------------------"

echo "8. pwd – print working directory"
pwd

echo "------------------------"

echo "9. mv – move/rename"
mv file.txt newfile.txt

echo "------------------------"

echo "10. cp – copy file"
cp newfile.txt backup.txt

echo "------------------------"

echo "11. rm – delete file"
echo "Command: rm file.txt"

echo "------------------------"

echo "12. touch – create file"
touch new.txt

echo "------------------------"

echo "13. chmod – change permission"
chmod 755 new.txt

echo "------------------------"

echo "14. chown – change owner"
echo "Command: chown user file.txt"

echo "------------------------"

echo "15. more – view file"
more newfile.txt

echo "------------------------"

echo "16. less – advanced viewer"
echo "Command: less newfile.txt"

echo "------------------------"

echo "17. find – search files"
find . -name "newfile.txt"

echo "------------------------"

echo "18. wc – count"
wc newfile.txt

echo "------------------------"

echo "19. cut – extract data"
cut -d ":" -f1 /etc/passwd

echo "------------------------"

echo "20. paste – merge files"
paste newfile.txt backup.txt

echo "------------------------"

echo "21. head – first lines"
head -n 5 newfile.txt

echo "------------------------"

echo "22. tail – last lines"
tail -n 5 newfile.txt

echo "------------------------"

echo "23. useradd – add user"
echo "Command: sudo useradd user1"

echo "------------------------"

echo "24. userdel – delete user"
echo "Command: sudo userdel user1"

echo "------------------------"

echo "25. usermod – modify user"
echo "Command: sudo usermod -aG sudo user1"

echo "------------------------"

echo "26. passwd – change password"
echo "Command: passwd user1"

echo "------------------------"

echo "27. top – system monitor"
echo "Command: top"

echo "------------------------"

echo "28. ps – process status"
ps aux

echo "------------------------"

echo "29. ssh – remote login"
echo "Command: ssh user@192.168.1.100"

echo "------------------------"

echo "30. scp – copy remotely"
echo "Command: scp file.txt user@192.168.1.100:/home/user"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E03_BasicLinuxCommands.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E03_BasicLinuxCommands.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E03_BasicLinuxCommands.sh
```

---

# ✅ Advantages

* Helps learn essential Linux commands
* Useful for system administration
* Demonstrates file and process handling
* Useful for networking operations

---

# ❌ Limitations

* Some commands require administrator privileges
* Certain networking commands need active network connection

---

# 📚 Viva Questions

## 1️⃣ What is Linux?

Linux is an open-source operating system.

---

## 2️⃣ What does `pwd` command do?

It displays current working directory.

---

## 3️⃣ What is the use of `chmod`?

It changes file permissions.

---

## 4️⃣ What is the difference between `cp` and `mv`?

`cp` copies files while `mv` moves or renames files.

---

## 5️⃣ What does `ps aux` display?

It displays all running processes.

---

# 🎓 Result

Thus, various basic Linux commands were studied and executed successfully.
