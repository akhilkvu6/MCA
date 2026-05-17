# 📘 README

<div align="center">

# 🖥️ E16_Palindrome

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to check whether a given number is a palindrome or not.

---

# 📘 Theory

A palindrome number is a number that remains the same when its digits are reversed.

Examples:

```text id="k2x8vr"
121 → Palindrome
454 → Palindrome
123 → Not Palindrome
```

In this experiment, the entered number is reversed using a `while` loop. The reversed number is then compared with the original number.

### Concepts Used

* Shell scripting
* While loop
* Conditional statements
* Arithmetic operations

---

# 🧠 Algorithm

1. Start
2. Read a number from the user
3. Store the original number in a temporary variable
4. Reverse the number using modulus and division operations
5. Compare reversed number with original number
6. If both are equal, display Palindrome
7. Otherwise display Not Palindrome
8. Stop

---

# 💻 Program

```bash id="x7m1qp"
#!/bin/bash

echo -n "Enter a Number: "
read n

temp=$n
rev=0

while (( n > 0 ))
do
    rem=$(( n % 10 ))
    rev=$(( rev * 10 + rem ))
    n=$(( n / 10 ))
done

if (( temp == rev ))
then
    echo "$temp is a Palindrome Number"
else
    echo "$temp is Not a Palindrome Number"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="q9w4td"
nano E16_Palindrome.sh
```

## 🔐 Give Execute Permission

```bash id="m3p8vk"
chmod +x E16_Palindrome.sh
```

## ▶️ Execute the Program

```bash id="j1x6rz"
./E16_Palindrome.sh
```

---

# 🖨️ Sample Output

```text id="h5n2qy"
Enter a Number: 121

121 is a Palindrome Number
```

---

# 🔍 Explanation

| Symbol / Command | Description            |
| ---------------- | ---------------------- |
| `while`          | Loop statement         |
| `%`              | Modulus operator       |
| `/`              | Division operator      |
| `if`             | Conditional statement  |
| `$(( ))`         | Arithmetic evaluation  |
| `temp=$n`        | Stores original number |

---

# ✅ Advantages

* Easy to understand logic
* Demonstrates loops and conditions clearly
* Useful for number manipulation concepts

---

# ❌ Limitations

* Works only for positive integers
* No validation for invalid input

---

# 📚 Viva Questions

## 1️⃣ What is a palindrome number?

A palindrome number remains the same when reversed.

---

## 2️⃣ Why is the original number stored in `temp`?

Because the original value changes during reversal process.

---

## 3️⃣ What is the use of `%` operator?

It extracts the last digit of a number.

---

## 4️⃣ Why is division by 10 used?

To remove the last digit from the number.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing commands in a file to automate Linux tasks.

---

# 🎓 Result

Thus, the shell script to check whether a given number is palindrome or not was executed successfully.
