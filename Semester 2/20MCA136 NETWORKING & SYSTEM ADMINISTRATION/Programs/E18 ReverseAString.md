# 📘 README

<div align="center">

# 🖥️ E18_ReverseAString

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to reverse a given string.

---

# 📘 Theory

String reversal means displaying the characters of a string in reverse order.

Example:

```text id="m4x8vq"
HELLO → OLLEH
```

In this experiment, the length of the string is calculated first. A `for` loop is then used to access characters from the end of the string to the beginning and form the reversed string.

### Concepts Used

* Shell scripting
* String manipulation
* For loop
* Parameter expansion

---

# 🧠 Algorithm

1. Start
2. Read a string from the user
3. Find the length of the string
4. Initialize an empty reverse string
5. Traverse the string from last character to first
6. Append each character to reverse string
7. Display reversed string
8. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo -n "Enter a String: "
read str

rev=""

len=${#str}

for (( i=len-1; i>=0; i-- ))
do
    rev="$rev${str:$i:1}"
done

echo "Reversed String = $rev"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E18_ReverseAString.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E18_ReverseAString.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E18_ReverseAString.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Enter a String: Linux

Reversed String = xuniL
```

---

# 🔍 Explanation

| Symbol / Command | Description            |
| ---------------- | ---------------------- |
| `${#str}`        | Finds string length    |
| `${str:$i:1}`    | Extracts one character |
| `for`            | Loop statement         |
| `read`           | Accepts input          |
| `echo`           | Displays output        |
| `rev`            | Stores reversed string |

---

# ✅ Advantages

* Simple and efficient logic
* Demonstrates string manipulation clearly
* Useful for learning loops and indexing

---

# ❌ Limitations

* Case-sensitive output
* No validation for empty string

---

# 📚 Viva Questions

## 1️⃣ What is string reversal?

String reversal means displaying characters in reverse order.

---

## 2️⃣ What does `${#str}` do?

It returns the length of the string.

---

## 3️⃣ What does `${str:$i:1}` mean?

It extracts one character from the string at a specified position.

---

## 4️⃣ Why is loop started from `len-1`?

Because string indexing starts from 0 and the last character index is `length - 1`.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to reverse a given string was executed successfully.
