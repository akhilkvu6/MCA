# 📘 README

<div align="center">

# 🖥️ E17_FibonacciSeries

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to generate the Fibonacci series.

---

# 📘 Theory

The Fibonacci series is a sequence in which each number is the sum of the two preceding numbers.

The sequence starts with:

```text id="k8v2mq"
0 1 1 2 3 5 8 13 ...
```

Formula:

```text id="m3x7tp"
F(n) = F(n-1) + F(n-2)
```

In this experiment, two variables are initialized with `0` and `1`. A `for` loop is used to generate the Fibonacci series up to the given limit.

### Concepts Used

* Shell scripting
* For loop
* Arithmetic operations
* Variable swapping

---

# 🧠 Algorithm

1. Start
2. Read the limit from the user
3. Initialize first number as 0
4. Initialize second number as 1
5. Repeat loop until limit is reached
6. Display current Fibonacci number
7. Find next Fibonacci number by adding previous two numbers
8. Update variables
9. Stop

---

# 💻 Program

```bash id="q7z1wp"
#!/bin/bash

echo -n "Enter Limit: "
read n

a=0
b=1

echo "Fibonacci Series:"

for (( i=0; i<n; i++ ))
do
    echo -n "$a "

    fn=$(( a + b ))
    a=$b
    b=$fn
done

echo
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="d5m8xr"
nano E17_FibonacciSeries.sh
```

## 🔐 Give Execute Permission

```bash id="t2v9pk"
chmod +x E17_FibonacciSeries.sh
```

## ▶️ Execute the Program

```bash id="h4x1qn"
./E17_FibonacciSeries.sh
```

---

# 🖨️ Sample Output

```text id="z7n3mf"
Enter Limit: 7

Fibonacci Series:
0 1 1 2 3 5 8
```

---

# 🔍 Explanation

| Symbol / Command | Description                   |
| ---------------- | ----------------------------- |
| `for`            | Loop statement                |
| `$(( ))`         | Arithmetic evaluation         |
| `echo -n`        | Prints output without newline |
| `read`           | Accepts user input            |
| `a` and `b`      | Store Fibonacci values        |

---

# ✅ Advantages

* Simple and efficient implementation
* Demonstrates looping and arithmetic concepts
* Useful for mathematical sequence generation

---

# ❌ Limitations

* Works only for positive limits
* Large limits may produce very large numbers

---

# 📚 Viva Questions

## 1️⃣ What is Fibonacci series?

It is a sequence where each number is the sum of the previous two numbers.

---

## 2️⃣ What are the first two Fibonacci numbers?

0 and 1.

---

## 3️⃣ Why are two variables used?

To store the previous two Fibonacci values.

---

## 4️⃣ What is the purpose of `echo -n`?

It prints output without moving to the next line.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to generate the Fibonacci series was executed successfully.
