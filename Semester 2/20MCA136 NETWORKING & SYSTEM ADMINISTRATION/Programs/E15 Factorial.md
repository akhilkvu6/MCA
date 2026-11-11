# 📘 README

<div align="center">

# 🖥️ E15_Factorial

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to find the factorial of a given number.

---

# 📘 Theory

Factorial of a number is the product of all positive integers from 1 to that number.

Mathematically,

```text id="l3x9pw"
n! = n × (n-1) × (n-2) × ... × 1
```

Example:

```text id="w7k2mv"
5! = 5 × 4 × 3 × 2 × 1 = 120
```

In this experiment, a `for` loop is used to repeatedly multiply numbers from 1 to `n`.

### Concepts Used

* Shell scripting
* For loop
* Arithmetic operations
* User input

---

# 🧠 Algorithm

1. Start
2. Read a number from the user
3. Initialize factorial variable as 1
4. Repeat loop from 1 to the entered number
5. Multiply factorial by loop variable
6. Store result in factorial variable
7. Display factorial value
8. Stop

---

# 💻 Program

```bash id="t5v0qn"
#!/bin/bash

echo -n "Enter a Number: "
read n

fact=1

for (( i=1; i<=n; i++ ))
do
    fact=$(( fact * i ))
done

echo "Factorial of $n = $fact"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="x4f8kj"
nano E15_Factorial.sh
```

## 🔐 Give Execute Permission

```bash id="q9m2pa"
chmod +x E15_Factorial.sh
```

## ▶️ Execute the Program

```bash id="v6z1rc"
./E15_Factorial.sh
```

---

# 🖨️ Sample Output

```text id="p3j7wb"
Enter a Number: 5

Factorial of 5 = 120
```

---

# 🔍 Explanation

| Symbol / Command | Description                    |
| ---------------- | ------------------------------ |
| `for`            | Loop statement                 |
| `$(( ))`         | Arithmetic evaluation          |
| `read`           | Accepts user input             |
| `echo`           | Displays output                |
| `fact=1`         | Initializes factorial variable |

---

# ✅ Advantages

* Simple and easy implementation
* Demonstrates looping concept clearly
* Useful for mathematical calculations

---

# ❌ Limitations

* Works only for positive integers
* Large numbers may exceed integer limit

---

# 📚 Viva Questions

## 1️⃣ What is factorial?

Factorial is the product of all positive integers from 1 to a given number.

---

## 2️⃣ What is the factorial of 0?

Factorial of 0 is 1.

---

## 3️⃣ Why is `fact` initialized to 1?

Because multiplication starts with identity value 1.

---

## 4️⃣ What is the use of `for` loop?

The `for` loop is used to repeat statements multiple times.

---

## 5️⃣ What does `$(( ))` do?

It performs arithmetic calculations in Bash.

---

# 🎓 Result

Thus, the shell script to find the factorial of a given number was executed successfully.
