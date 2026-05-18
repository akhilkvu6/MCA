# 📘 README

<div align="center">

# 🖥️ E08_EvenOrOdd

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to check whether a number is even or odd.

---

# 📘 Theory

An even number is divisible by 2 without remainder, while an odd number leaves remainder 1 when divided by 2.

This program uses the modulus operator `%` to determine whether the entered number is even or odd.

### Concepts Used

* Shell scripting
* Conditional statements
* Modulus operator
* Arithmetic evaluation

---

# 🧠 Algorithm

1. Start
2. Read a number from the user
3. Divide the number by 2
4. Check the remainder
5. If remainder is 0, display Even
6. Otherwise display Odd
7. Stop

---

# 💻 Program

```bash id="lc74bx"
#!/bin/bash

echo -n "Enter a Number: "
read n

if (( n % 2 == 0 ))
then
    echo "$n is an Even Number"
else
    echo "$n is an Odd Number"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="oqj0tz"
nano E08_EvenOrOdd.sh
```

## 🔐 Give Execute Permission

```bash id="yk8fgf"
chmod +x E08_EvenOrOdd.sh
```

## ▶️ Execute the Program

```bash id="hz2jlo"
./E08_EvenOrOdd.sh
```

---

# 🖨️ Sample Output

```text id="22z7ai"
Enter a Number: 15

15 is an Odd Number
```

---

# 🔍 Explanation

| Symbol / Command | Description               |
| ---------------- | ------------------------- |
| `read`           | Accepts input from user   |
| `echo`           | Displays output           |
| `%`              | Modulus operator          |
| `if`             | Decision-making statement |
| `(( ))`          | Arithmetic evaluation     |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates arithmetic and conditions
* Useful for beginners in shell scripting

---

# ❌ Limitations

* Works only for numeric values
* No input validation included

---

# 📚 Viva Questions

## 1️⃣ What is an even number?

An even number is divisible by 2 without remainder.

---

## 2️⃣ What is an odd number?

An odd number leaves remainder 1 when divided by 2.

---

## 3️⃣ What does `%` operator do?

It returns the remainder after division.

---

## 4️⃣ What is `(( ))` in Bash?

It is used for arithmetic evaluation.

---

## 5️⃣ What is the purpose of `if` statement?

It is used for decision making.

---

# 🎓 Result

Thus, the shell script to check whether a number is even or odd was executed successfully.
