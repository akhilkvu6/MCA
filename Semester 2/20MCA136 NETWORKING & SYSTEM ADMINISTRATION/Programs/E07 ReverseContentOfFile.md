# 📘 README

<div align="center">

# 🖥️ E07_ReverseContentOfFile

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to display the reverse content of a file.

---

# 📘 Theory

Files in Linux store data line by line.

The `tac` command is used to display the contents of a file in reverse order line-by-line.

This experiment accepts a filename as a command-line argument and checks:

* whether the file exists
* whether it is a regular file

If valid, the script displays:

1. Original content
2. Reversed content using `tac`

### Concepts Used

* Shell scripting
* Command-line arguments
* File checking
* `tac` command
* Conditional statements

---

# 🧠 Algorithm

1. Start
2. Check whether exactly one argument is provided
3. Check whether the file exists using `-f`
4. Display original file contents
5. Display reversed file contents using `tac`
6. Otherwise display error message
7. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

if [ $# -eq 1 ]
then
    if [ -f "$1" ]
    then
        echo "Contents of $1"
        cat "$1"

        echo "Reverse of $1"
        tac "$1"
    else
        echo "File does not exist!!"
    fi
else
    echo "Usage: $0 <filename>"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E07_ReverseContentOfFile.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E07_ReverseContentOfFile.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E07_ReverseContentOfFile.sh sample.txt
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Contents of sample.txt

Linux
Shell
Programming

Reverse of sample.txt

Programming
Shell
Linux
```

---

# 🔍 Explanation

| Symbol / Command | Description                      |
| ---------------- | -------------------------------- |
| `$#`             | Number of command-line arguments |
| `$1`             | First command-line argument      |
| `-eq`            | Equality comparison              |
| `-f`             | Checks whether file exists       |
| `cat`            | Displays file contents           |
| `tac`            | Displays file in reverse order   |
| `if`             | Conditional statement            |

---

# ✅ Advantages

* Simple and efficient file processing
* Demonstrates command-line arguments
* Useful for learning file handling in Linux

---

# ❌ Limitations

* Works only with text files
* Reverses lines, not characters inside lines

---

# 📚 Viva Questions

## 1️⃣ What is `$#` in shell scripting?

It stores the number of command-line arguments.

---

## 2️⃣ What does `$1` represent?

It represents the first command-line argument.

---

## 3️⃣ What is the purpose of `-f`?

It checks whether the given file exists and is a regular file.

---

## 4️⃣ What is the difference between `cat` and `tac`?

`cat` displays file normally, while `tac` displays file in reverse line order.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to display the reverse content of a file was executed successfully.
