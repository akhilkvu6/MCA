# 📘 README

<div align="center">

# 🖥️ E12_CombineStrings

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to combine two strings.

---

# 📘 Theory

String concatenation means joining two or more strings together to form a single string.

In shell scripting, strings can be combined simply by placing them together inside double quotes.

Example:

```text id="m4x8vq"
Hello + World = HelloWorld
```

This experiment reads two strings from the user and combines them into a single string.

### Concepts Used

* Shell scripting
* User input
* String concatenation
* Variables

---

# 🧠 Algorithm

1. Start
2. Read first string from the user
3. Read second string from the user
4. Concatenate both strings
5. Store result in a variable
6. Display the combined string
7. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo -n "Enter First String: "
read str1

echo -n "Enter Second String: "
read str2

result="$str1$str2"

echo "Combined String = $result"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E12_CombineStrings.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E12_CombineStrings.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E12_CombineStrings.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Enter First String: Hello
Enter Second String: World

Combined String = HelloWorld
```

---

# 🔍 Explanation

| Symbol / Command | Description             |
| ---------------- | ----------------------- |
| `read`           | Accepts input from user |
| `echo`           | Displays output         |
| `str1`           | Stores first string     |
| `str2`           | Stores second string    |
| `result`         | Stores combined string  |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates string handling in shell scripting
* Useful for beginners

---

# ❌ Limitations

* No space added automatically between strings
* No validation for empty input

---

# 📚 Viva Questions

## 1️⃣ What is string concatenation?

String concatenation means joining strings together.

---

## 2️⃣ What is the purpose of double quotes?

Double quotes allow variable expansion in shell scripting.

---

## 3️⃣ What does `read` command do?

It accepts input from the user.

---

## 4️⃣ What is a variable?

A variable is used to store data temporarily.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to combine two strings was executed successfully.
