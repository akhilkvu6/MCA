# 📘 README

<div align="center">

# 🖥️ E09_CheckDictionary

### NSA Lab – Shell Scripting

</div>

---

# 🎯 Aim

To write a shell script to check whether a word exists in the dictionary.

---

# 📘 Theory

A dictionary file contains a list of valid words stored in the system.

In Linux systems, the file:

```text id="m4x8vq"
/usr/share/dict/words
```

contains dictionary words.

This experiment uses the `grep` command to search for a word entered by the user.

### Concepts Used

* Shell scripting
* File searching
* `grep` command
* Conditional statements

---

# 🧠 Algorithm

1. Start
2. Read a word from the user
3. Search the word in dictionary file using `grep`
4. If the word exists, display success message
5. Otherwise display not found message
6. Stop

---

# 💻 Program

```bash id="p7n2qw"
#!/bin/bash

echo -n "Enter a Word: "
read word

if grep -wq "$word" /usr/share/dict/words
then
    echo "$word exists in dictionary"
else
    echo "$word does not exist in dictionary"
fi
```

---

# ⚙️ Commands Used

## 📄 Create Script File

```bash id="k3v9xp"
nano E09_CheckDictionary.sh
```

## 🔐 Give Execute Permission

```bash id="t5m1zr"
chmod +x E09_CheckDictionary.sh
```

## ▶️ Execute the Program

```bash id="x8q4vn"
./E09_CheckDictionary.sh
```

---

# 🖨️ Sample Output

```text id="d6p2wk"
Enter a Word: Linux

Linux exists in dictionary
```

---

# 🔍 Explanation

| Symbol / Command        | Description            |
| ----------------------- | ---------------------- |
| `grep`                  | Searches text in files |
| `-w`                    | Matches whole word     |
| `-q`                    | Quiet mode (no output) |
| `if`                    | Conditional statement  |
| `/usr/share/dict/words` | Dictionary file path   |

---

# ✅ Advantages

* Simple and efficient searching
* Demonstrates file handling and searching concepts
* Useful for learning Linux commands

---

# ❌ Limitations

* Depends on dictionary file availability
* Case-sensitive search

---

# 📚 Viva Questions

## 1️⃣ What is `grep` command?

`grep` is used to search text patterns in files.

---

## 2️⃣ What does `-w` option do?

It matches only complete words.

---

## 3️⃣ What does `-q` option do?

It suppresses normal output and works in quiet mode.

---

## 4️⃣ What is `/usr/share/dict/words`?

It is a dictionary file containing words in Linux systems.

---

## 5️⃣ What is shell scripting?

Shell scripting is writing Linux commands in a file to automate tasks.

---

# 🎓 Result

Thus, the shell script to check whether a word exists in the dictionary was executed successfully.
