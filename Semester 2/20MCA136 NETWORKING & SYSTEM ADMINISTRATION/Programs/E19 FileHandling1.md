# 📘 README

<div align="center">

# 🖥️ E19_FileHandling1

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to perform basic file handling operations.

### Operations Performed

1. Create and copy a file
2. Print file contents from a certain line
3. Find differences between two files
4. Print lines matching a specific pattern

---

# 📘 Theory

File handling is an important concept in Linux shell scripting.

Linux provides several commands for performing operations on files such as:

| Command | Purpose                 |
| ------- | ----------------------- |
| `cat`   | Create/display file     |
| `cp`    | Copy file               |
| `tail`  | Print from certain line |
| `diff`  | Compare two files       |
| `grep`  | Pattern matching        |

This experiment demonstrates different file manipulation techniques using shell scripting and menu-driven programming.

---

# 🧠 Algorithm

1. Start
2. Display menu options
3. Read user choice
4. Perform selected operation using `case` statement
5. If choice is:

   * Create & Copy → create file and copy it
   * Print from Line → display file from specified line
   * Difference → compare two files
   * Pattern Matching → search matching lines
6. Display result
7. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo "1. Create and Copy File"
echo "2. Print from Certain Line"
echo "3. Difference Between Two Files"
echo "4. Pattern Matching"

read -p "Enter Choice: " ch

case $ch in

1)
    read -p "Enter File Name: " f1

    echo "Enter Profile Details:"
    cat > "$f1"

    read -p "Enter Existing File Name to Copy Into: " f2

    cp "$f1" "$f2"

    echo "File copied successfully"
    ;;

2)
    read -p "Enter File Name: " file
    read -p "Enter Starting Line Number: " line

    tail -n +"$line" "$file"
    ;;

3)
    read -p "Enter First File Name: " f1
    read -p "Enter Second File Name: " f2

    diff "$f1" "$f2"
    ;;

4)
    read -p "Enter File Name: " file
    read -p "Enter Pattern: " pattern

    grep -n "$pattern" "$file"
    ;;

*)
    echo "Invalid Choice"
    ;;

esac
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E19_FileHandling1.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E19_FileHandling1.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E19_FileHandling1.sh
```

---

# 🖨️ Sample Output

## 🔹 Create and Copy File

```text id="d6p2wk"
1. Create and Copy File
2. Print from Certain Line
3. Difference Between Two Files
4. Pattern Matching

Enter Choice: 1
Enter File Name: profile.txt

Enter Profile Details:
Akhil MCA
^D

Enter Existing File Name to Copy Into: backup.txt

File copied successfully
```

---

## 🔹 Print from Certain Line

```text id="m4x8vq"
Enter Choice: 2
Enter File Name: profile.txt
Enter Starting Line Number: 2
```

---

## 🔹 Difference Between Two Files

```text id="v7n2zk"
Enter Choice: 3
Enter First File Name: a.txt
Enter Second File Name: b.txt
```

---

## 🔹 Pattern Matching

```text id="q9p1wr"
Enter Choice: 4
Enter File Name: profile.txt
Enter Pattern: MCA
```

---

# 🔍 Explanation

| Command      | Description                                 |
| ------------ | ------------------------------------------- |
| `cat > file` | Creates file and accepts input              |
| `cp`         | Copies file                                 |
| `tail -n +n` | Prints from specified line                  |
| `diff`       | Shows differences between files             |
| `grep -n`    | Searches matching pattern with line numbers |
| `case`       | Menu-driven selection                       |

---

# ✅ Advantages

* Demonstrates multiple file handling operations
* Easy menu-driven implementation
* Useful for Linux file management practice

---

# ❌ Limitations

* No advanced error handling
* Requires valid file names and paths

---

# 📚 Viva Questions

## 1️⃣ What is the use of `cp` command?

It copies files from one location to another.

---

## 2️⃣ What does `tail -n +n` do?

It prints file contents starting from a specific line.

---

## 3️⃣ What is the purpose of `diff`?

It compares two files and displays differences.

---

## 4️⃣ What does `grep` command do?

It searches for matching text patterns in files.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to perform file handling operations was executed successfully.
