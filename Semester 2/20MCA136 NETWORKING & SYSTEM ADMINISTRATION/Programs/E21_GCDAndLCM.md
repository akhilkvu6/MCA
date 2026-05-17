# 📘 README

<div align="center">

# 🖥️ E21_GCDAndLCM

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to find the GCD and LCM of two numbers.

---

# 📘 Theory

### GCD (Greatest Common Divisor)

GCD is the largest positive integer that divides both numbers exactly.

Example:

```text id="k2m8vq"
GCD of 12 and 18 = 6
```

### LCM (Least Common Multiple)

LCM is the smallest positive integer that is divisible by both numbers.

Example:

```text id="n4x7zp"
LCM of 12 and 18 = 36
```

This program uses the Euclidean Algorithm to efficiently calculate the GCD.

Formula used for LCM:

```text id="r5v1mq"
LCM = (Number1 × Number2) / GCD
```

### Concepts Used

* Shell scripting
* While loop
* Arithmetic operations
* Euclidean Algorithm

---

# 🧠 Algorithm

1. Start
2. Read two numbers from the user
3. Store numbers in temporary variables
4. Repeat until second number becomes 0
5. Find remainder using modulus operator
6. Update values
7. Store final value as GCD
8. Calculate LCM using formula
9. Display GCD and LCM
10. Stop

---

# 💻 Program

```bash id="x9p2wt"
#!/bin/bash

echo -n "Enter First Number: "
read n1

echo -n "Enter Second Number: "
read n2

a=$n1
b=$n2

while (( b != 0 ))
do
    temp=$b
    b=$(( a % b ))
    a=$temp
done

gcd=$a
lcm=$(( (n1 * n2) / gcd ))

echo "GCD = $gcd"
echo "LCM = $lcm"
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="d7q1vk"
nano E21_GCDAndLCM.sh
```

## 🔐 Give Execute Permission

```bash id="m8x4pr"
chmod +x E21_GCDAndLCM.sh
```

## ▶️ Execute the Program

```bash id="v2n9qw"
./E21_GCDAndLCM.sh
```

---

# 🖨️ Sample Output

```text id="h3z8tm"
Enter First Number: 12
Enter Second Number: 18

GCD = 6
LCM = 36
```

---

# 🔍 Explanation

| Symbol / Command | Description                     |
| ---------------- | ------------------------------- |
| `while`          | Loop statement                  |
| `%`              | Modulus operator                |
| `$(( ))`         | Arithmetic evaluation           |
| `read`           | Accepts user input              |
| `echo`           | Displays output                 |
| `temp`           | Temporary variable for swapping |

---

# ✅ Advantages

* Efficient and optimized algorithm
* Faster than traditional divisor checking
* Demonstrates looping and arithmetic concepts clearly

---

# ❌ Limitations

* Works only for integer values
* No validation for invalid input

---

# 📚 Viva Questions

## 1️⃣ What is GCD?

GCD is the largest number that divides two numbers exactly.

---

## 2️⃣ What is LCM?

LCM is the smallest number divisible by both numbers.

---

## 3️⃣ What is Euclidean Algorithm?

It is an efficient method for finding GCD using repeated remainder operations.

---

## 4️⃣ What is the formula used to find LCM?

```text id="j4m7xp"
LCM = (a × b) / GCD
```

---

## 5️⃣ Why is modulus operator used?

It is used to find the remainder during GCD calculation.

---

# 🎓 Result

Thus, the shell script to find the GCD and LCM of two numbers was executed successfully.
