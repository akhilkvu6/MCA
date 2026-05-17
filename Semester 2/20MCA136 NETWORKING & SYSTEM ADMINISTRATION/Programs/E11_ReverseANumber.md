# 📘 README

<div align="center">

# 🖥️ E11_ReverseANumber

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to reverse a given number.

---

# 📘 Theory

Reversing a number means arranging its digits in reverse order.

This program uses a `while` loop along with arithmetic operations to extract digits one by one and form the reversed number.

### Concepts Used

* Shell scripting
* While loop
* Arithmetic operations
* Modulus operator

---

# 🧠 Algorithm

1. Start
2. Read a number from the user
3. Initialize reverse variable as 0
4. Extract the last digit using modulus operator
5. Append the digit to the reversed number
6. Remove the last digit from original number
7. Repeat until number becomes 0
8. Display reversed number
9. Stop

---

# 💻 Program

```bash id="n5p2qx"
#!/bin/bash

echo -n "Enter a Number: "
read n

rev=0

while (( n > 0 ))
do
    rem=$(( n % 10 ))
    rev=$(( rev * 10 + rem ))
    n=$(( n / 10 ))
done

echo "Reversed Number = $rev"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="4f1jpd"
nano E11_ReverseANumber.sh
```

## 🔐 Give Execute Permission

```bash id="y8w2kt"
chmod +x E11_ReverseANumber.sh
```

## ▶️ Execute the Program

```bash id="l9s3vm"
./E11_ReverseANumber.sh
```

---

# 🖨️ Sample Output

```text id="h7n0qb"
Enter a Number: 12345

Reversed Number = 54321
```

---

# 🔍 Explanation

| Symbol / Command | Description           |
| ---------------- | --------------------- |
| `while`          | Loop statement        |
| `%`              | Modulus operator      |
| `/`              | Division operator     |
| `$(( ))`         | Arithmetic evaluation |
| `read`           | Accepts user input    |
| `echo`           | Displays output       |

---

# ✅ Advantages

* Simple and efficient logic
* Demonstrates loop and arithmetic operations
* Easy to understand for beginners

---

# ❌ Limitations

* Works only for positive integers
* No input validation included

---

# 📚 Viva Questions

## 1️⃣ What is the purpose of `%` operator?

It returns the remainder after division.

---

## 2️⃣ Why is while loop used?

The loop repeats until the number becomes 0.

---

## 3️⃣ How is the last digit extracted?

Using modulus operation with 10.

---

## 4️⃣ How is the last digit removed?

Using integer division by 10.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to reverse a given number was executed successfully.
