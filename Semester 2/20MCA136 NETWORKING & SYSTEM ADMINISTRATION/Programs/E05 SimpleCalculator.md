<div align="center">

# 🖥️ E05_SimpleCalculator

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to perform basic arithmetic operations using a simple calculator.

---

# 📘 Theory

A calculator program is used to perform arithmetic operations such as addition, subtraction, multiplication, and division.

In this experiment, the shell script accepts two numbers and a user choice. Based on the selected operation, the script performs the corresponding arithmetic calculation using the `case` statement.

### Concepts Used

* Shell scripting
* User input
* Arithmetic operations
* `case` statement
* Conditional statements

---

# 🧠 Algorithm

1. Start
2. Read two numbers from the user
3. Display calculator menu
4. Read user choice
5. Use `case` statement to perform selected operation
6. Display the result
7. Stop

---

# 💻 Program

```bash id="9h3mzy"
#!/bin/bash

echo "===== SIMPLE CALCULATOR ====="

echo -n "Enter First Number: "
read n1

echo -n "Enter Second Number: "
read n2

echo "Choose Operation"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"

echo -n "Enter Choice: "
read ch

case $ch in
    1)
        result=$((n1 + n2))
        echo "Result = $result"
        ;;
    2)
        result=$((n1 - n2))
        echo "Result = $result"
        ;;
    3)
        result=$((n1 * n2))
        echo "Result = $result"
        ;;
    4)
        if [[ $n2 -eq 0 ]]
        then
            echo "Division by zero is not possible"
        else
            result=$((n1 / n2))
            echo "Result = $result"
        fi
        ;;
    *)
        echo "Invalid Choice"
        ;;
esac
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="sy2twr"
nano E05_SimpleCalculator.sh
```

## 🔐 Give Execute Permission

```bash id="hjgax7"
chmod +x E05_SimpleCalculator.sh
```

## ▶️ Execute the Program

```bash id="3muj86"
./E05_SimpleCalculator.sh
```

---

# 🖨️ Sample Output

```text id="w9i5jf"
===== SIMPLE CALCULATOR =====

Enter First Number: 20
Enter Second Number: 10

Choose Operation
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter Choice: 1

Result = 30
```

---

# 🔍 Explanation

| Command / Symbol | Description                  |
| ---------------- | ---------------------------- |
| `read`           | Accepts user input           |
| `echo`           | Displays output              |
| `case`           | Multi-way decision statement |
| `$(( ))`         | Arithmetic operation syntax  |
| `;;`             | Terminates case block        |
| `if`             | Conditional statement        |

---

# ✅ Advantages

* Easy to understand and execute
* Demonstrates arithmetic operations in shell scripting
* Uses menu-driven approach

---

# ❌ Limitations

* Supports only integer calculations
* Limited to four operations

---

# 📚 Viva Questions

## 1️⃣ What is a shell script?

A shell script is a file containing Linux commands executed by the shell interpreter.

---

## 2️⃣ What is the use of `case` statement?

The `case` statement is used for multi-way branching based on user choice.

---

## 3️⃣ What does `$(( ))` represent?

It is used for arithmetic calculations in shell scripting.

---

## 4️⃣ Why is division by zero checked?

Division by zero is mathematically undefined and causes errors.

---

## 5️⃣ What is the purpose of `;;` in case statement?

It terminates a particular case block.

---

# 🎓 Result

Thus, the shell script to implement a simple calculator was executed successfully.
