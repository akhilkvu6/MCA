# 📘 README

<div align="center">

# 🖥️ E13_Substring

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to extract a substring from a given string.

---

# 📘 Theory

A substring is a part of a string extracted from a specified position with a specified length.

In Bash shell scripting, substring extraction is performed using parameter expansion syntax:

```text id="m4v8xp"
${string:start:length}
```

Where:

* `string` → Original string
* `start` → Starting index position
* `length` → Number of characters to extract

### Concepts Used

* Shell scripting
* String manipulation
* Parameter expansion
* User input

---

# 🧠 Algorithm

1. Start
2. Read a string from the user
3. Read starting position
4. Read substring length
5. Extract substring using parameter expansion
6. Store substring in a variable
7. Display substring
8. Stop

---

# 💻 Program

```bash id="q8n2vk"
#!/bin/bash

echo -n "Enter a String: "
read str

echo -n "Enter Starting Position: "
read pos

echo -n "Enter Length: "
read len

substr=${str:$pos:$len}

echo "Substring = $substr"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="t3m9wr"
nano E13_Substring.sh
```

## 🔐 Give Execute Permission

```bash id="v6x1qp"
chmod +x E13_Substring.sh
```

## ▶️ Execute the Program

```bash id="p7k4zn"
./E13_Substring.sh
```

---

# 🖨️ Sample Output

```text id="h2v8qm"
Enter a String: Programming
Enter Starting Position: 3
Enter Length: 4

Substring = gram
```

---

# 🔍 Explanation

| Symbol / Command   | Description                |
| ------------------ | -------------------------- |
| `read`             | Accepts input from user    |
| `echo`             | Displays output            |
| `${str:$pos:$len}` | Extracts substring         |
| `substr`           | Stores extracted substring |

---

# ✅ Advantages

* Simple and efficient method
* Demonstrates string manipulation clearly
* Useful for text processing operations

---

# ❌ Limitations

* Invalid positions may produce empty output
* No validation for incorrect input

---

# 📚 Viva Questions

## 1️⃣ What is a substring?

A substring is a smaller part extracted from a string.

---

## 2️⃣ What is parameter expansion?

It is a Bash feature used for string manipulation and variable operations.

---

## 3️⃣ What does `${str:$pos:$len}` do?

It extracts characters from a string starting at a given position for a specified length.

---

## 4️⃣ What is indexing in strings?

Indexing refers to character positions in a string starting from 0.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to extract a substring from a given string was executed successfully.
