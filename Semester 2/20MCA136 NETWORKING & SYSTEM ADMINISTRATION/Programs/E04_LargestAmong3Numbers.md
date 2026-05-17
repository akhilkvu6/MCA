<div align="center">

# 🖥️ E04_LargestAmong3Numbers

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to find the largest among three numbers.

---

# 📘 Theory

Shell scripting is used to automate tasks in Linux using commands and programming constructs.

In this experiment, the user enters three numbers. The program compares the numbers using conditional statements and displays the largest number.

### Concepts Used

* `if`, `elif`, `else`
* Comparison operators
* Logical AND operator
* User input using `read`

---

# 🧠 Algorithm

1. Start
2. Read three numbers from the user
3. Compare the first number with the other two numbers
4. If the first number is largest, display it
5. Otherwise compare the second number with the other two numbers
6. If the second number is largest, display it
7. Else display the third number
8. Stop

---

# 💻 Program

```bash id="zv0n3s"
#!/bin/bash

echo -n "Enter Number 1: "
read n1

echo -n "Enter Number 2: "
read n2

echo -n "Enter Number 3: "
read n3

if [[ $n1 -ge $n2 && $n1 -ge $n3 ]]
then
    echo "$n1 is the largest number"
elif [[ $n2 -ge $n1 && $n2 -ge $n3 ]]
then
    echo "$n2 is the largest number"
else
    echo "$n3 is the largest number"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="pk8wo4"
nano E04_LargestAmong3Numbers.sh
```

## 🔐 Give Execute Permission

```bash id="7g8qqm"
chmod +x E04_LargestAmong3Numbers.sh
```

## ▶️ Execute the Program

```bash id="32i2qj"
./E04_LargestAmong3Numbers.sh
```

---

# 🖨️ Sample Output

```text id="w4zjdc"
Enter Number 1: 25
Enter Number 2: 90
Enter Number 3: 45

90 is the largest number
```

---

# 🔍 Explanation

| Command / Symbol | Description                      |
| ---------------- | -------------------------------- |
| `#!/bin/bash`    | Specifies Bash shell interpreter |
| `echo`           | Displays output                  |
| `read`           | Accepts user input               |
| `[[ ]]`          | Used for conditional checking    |
| `-ge`            | Greater than or equal to         |
| `&&`             | Logical AND operator             |

---

# ✅ Advantages

* Simple and easy to understand
* Demonstrates conditional statements clearly
* Useful for beginners in shell scripting

---

# ❌ Limitations

* Accepts only numeric values
* Does not validate invalid inputs

---

# 📚 Viva Questions

## 1️⃣ What is a shell script?

A shell script is a file containing Linux commands and scripting statements executed by the shell.

---

## 2️⃣ What is the purpose of `#!/bin/bash`?

It specifies that the script should run using the Bash shell interpreter.

---

## 3️⃣ What does `-ge` represent?

`-ge` means greater than or equal to.

---

## 4️⃣ What is the use of `read` command?

It is used to take input from the user.

---

## 5️⃣ What is `&&` operator?

It is the logical AND operator used to combine multiple conditions.

---

# 🎓 Result

Thus, the shell script to find the largest among three numbers was executed successfully.
