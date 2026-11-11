# 📘 README

<div align="center">

# 🖥️ E23_FileHandling2

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To perform file handling operations using Linux commands.

### Operations Performed

1. Create a file using `cat`
2. Display first two lines
3. Display last two lines
4. Copy a file
5. Count lines, words, and characters
6. Display a specific line
7. Append contents to another file

---

# 📘 Theory

Linux provides several commands for handling files efficiently.

| Command | Purpose                        |
| ------- | ------------------------------ |
| `cat`   | Create/display file            |
| `head`  | Display first lines            |
| `tail`  | Display last lines             |
| `cp`    | Copy files                     |
| `wc`    | Count lines, words, characters |
| `sed`   | Print specific lines           |
| `>>`    | Append content                 |

This experiment demonstrates multiple file handling operations using shell scripting.

---

# 🧠 Algorithm

1. Start
2. Create a file using `cat`
3. Display first two rows using `head`
4. Display last two rows using `tail`
5. Copy file using `cp`
6. Count lines, words, and characters using `wc`
7. Display third row using `sed`
8. Append contents to another file
9. Display success messages
10. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

# 1. Create file
cat > myfile <<EOF
1001 RAM 97
1002 NEHA 89
1010 DIVYA 77
1025 RAHUL 65
1012 ARUN 99
1013 NISHA 76
EOF

echo "------------------------"

# 2. First 2 rows
echo "First 2 rows:"
head -2 myfile

echo "------------------------"

# 3. Last 2 rows
echo "Last 2 rows:"
tail -2 myfile

echo "------------------------"

# 4. Copy file
cp myfile mycopyfile
echo "File copied to mycopyfile"

echo "------------------------"

# 5. Count
echo "Lines: $(wc -l < myfile)"
echo "Words: $(wc -w < myfile)"
echo "Characters: $(wc -c < myfile)"

echo "------------------------"

# 6. 3rd row
echo "3rd row:"
sed -n '3p' myfile

echo "------------------------"

# 7. Append
cat myfile >> myappendfile
echo "Content appended to myappendfile"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E23_FileHandling2.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E23_FileHandling2.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E23_FileHandling2.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
First 2 rows:
1001 RAM 97
1002 NEHA 89

Last 2 rows:
1012 ARUN 99
1013 NISHA 76

File copied to mycopyfile

Lines: 6
Words: 18
Characters: 90

3rd row:
1010 DIVYA 77

Content appended to myappendfile
```

---

# 🔍 Explanation

| Command       | Description            |
| ------------- | ---------------------- |
| `cat >`       | Creates file           |
| `head -2`     | Displays first 2 lines |
| `tail -2`     | Displays last 2 lines  |
| `cp`          | Copies file            |
| `wc -l`       | Counts lines           |
| `wc -w`       | Counts words           |
| `wc -c`       | Counts characters      |
| `sed -n '3p'` | Prints third line      |
| `>>`          | Appends contents       |

---

# ✅ Advantages

* Demonstrates multiple file handling operations
* Easy to understand and execute
* Useful for Linux file management practice

---

# ❌ Limitations

* Uses fixed sample data
* No advanced error handling included

---

# 📚 Viva Questions

## 1️⃣ What is the purpose of `head` command?

It displays the first few lines of a file.

---

## 2️⃣ What does `tail` command do?

It displays the last few lines of a file.

---

## 3️⃣ What is the use of `wc` command?

It counts lines, words, and characters.

---

## 4️⃣ What does `sed -n '3p'` do?

It prints the third line of a file.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to perform various file handling operations was executed successfully.

---

