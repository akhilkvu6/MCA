<div align="center">

# JAVA INSTALLATION GUIDE
## Windows Setup for Java Development

</div>

---

# Introduction

Java is a high-level, object-oriented programming language developed by Sun Microsystems (now owned by Oracle).

Java is widely used for:
- Desktop Applications
- Web Applications
- Android Development
- Enterprise Applications
- Scientific Applications

To develop Java programs, we need:
- Java Development Kit (JDK)
- Code Editor / IDE

---

# Requirements

Before installing Java, ensure:

- Windows 10 / Windows 11
- Internet Connection
- Administrator Access

---

# Software Required

| Software | Purpose |
|---|---|
| JDK (Java Development Kit) | Compile and Run Java Programs |
| VS Code | Code Editor |
| Java Extension Pack | Java Support in VS Code |

---

# Step 1 - Download Java JDK

Open browser and visit:

```text
https://www.oracle.com/java/technologies/downloads/
```

Download:

```text
JDK for Windows x64 Installer
```

Recommended Version:

```text
Java JDK 17 or Later
```

---

# Step 2 - Install Java JDK

1. Open downloaded installer file.

Example:

```text
jdk-17_windows-x64_bin.exe
```

2. Click:

```text
Next
```

3. Choose installation directory.

Default Location:

```text
C:\Program Files\Java\jdk-17
```

4. Click:

```text
Install
```

5. Wait for installation to complete.

6. Click:

```text
Close
```

---

# Step 3 - Verify Installation Directory

Open:

```text
C:\Program Files\Java\
```

You should see:

```text
jdk-17
```

---

# Step 4 - Configure Environment Variables

Environment variables help Windows locate Java commands globally.

---

# Open Environment Variables

1. Press:

```text
Windows + S
```

2. Search:

```text
Environment Variables
```

3. Open:

```text
Edit the system environment variables
```

4. Click:

```text
Environment Variables
```

---

# Step 5 - Set JAVA_HOME Variable

Under:

```text
System Variables
```

Click:

```text
New
```

Add:

| Variable Name | Variable Value |
|---|---|
| JAVA_HOME | C:\Program Files\Java\jdk-17 |

Click:

```text
OK
```

---

# Step 6 - Add Java to PATH

1. Under:

```text
System Variables
```

Select:

```text
Path
```

2. Click:

```text
Edit
```

3. Click:

```text
New
```

4. Add:

```text
%JAVA_HOME%\bin
```

5. Click:

```text
OK
```

6. Click:

```text
OK
```

again to save all changes.

---

# Step 7 - Verify Java Installation

Open Command Prompt.

Run:

```bash
java -version
```

Expected Output:

```text
java version "17.0.10"
```

---

# Step 8 - Verify Java Compiler

Run:

```bash
javac -version
```

Expected Output:

```text
javac 17.0.10
```

---

# JDK vs JRE vs JVM

| Component | Full Form | Purpose |
|---|---|---|
| JDK | Java Development Kit | Develop Java Programs |
| JRE | Java Runtime Environment | Run Java Programs |
| JVM | Java Virtual Machine | Executes Java Bytecode |

---

# Install Visual Studio Code

Download VS Code from:

```text
https://code.visualstudio.com/
```

Install using default settings.

---

# Install Java Extensions in VS Code

## Step 1

Open VS Code.

---

## Step 2

Open Extensions:

```text
Ctrl + Shift + X
```

---

## Step 3

Search:

```text
Extension Pack for Java
```

Install extension published by Microsoft.

---

# Features After Installing Java Extensions

- Syntax Highlighting
- Auto Completion
- Error Detection
- Debugging
- Java Project Support

---

# Creating First Java Program

Create file:

```text
HelloWorld.java
```

Code:

```java
class HelloWorld
{
    public static void main(String[] args)
    {
        System.out.println("Hello World");
    }
}
```

---

# Compile Java Program

Open terminal inside program folder.

Run:

```bash
javac HelloWorld.java
```

Generated File:

```text
HelloWorld.class
```

---

# Run Java Program

Run:

```bash
java HelloWorld
```

Output:

```text
Hello World
```

---

# Compile and Run Lab Programs

## Compile

```bash
javac P1_CompareObjects.java
```

---

## Run

```bash
java P1_CompareObjects
```

---

# Recommended Folder Structure

```text
MCA/
│
├── Semester 2/
│   ├── 20MCA132 OBJECT ORIENTED PROGRAMMING LAB/
│   │
│   │   ├── Installation/
│   │   │   └── Java_Installation.md
│   │   │
│   │   └── Programs/
│   │       ├── README.md
│   │       ├── P1_CompareObjects.java
│   │       ├── P1_CompareObjects.md
│   │       └── ...
```

---

# Common Errors and Solutions

## 1. java is not recognized

### Reason

PATH variable not configured correctly.

### Solution

Add:

```text
%JAVA_HOME%\bin
```

to PATH variable.

---

## 2. javac is not recognized

### Reason

JDK not installed properly.

### Solution

Install JDK instead of JRE.

---

## 3. ClassNotFoundException

### Reason

Incorrect class name while running program.

### Wrong

```bash
java HelloWorld.java
```

### Correct

```bash
java HelloWorld
```

---

## 4. Public Class Name Mismatch

### Wrong

```text
File: Test.java
public class Hello
```

### Correct

```text
File: Hello.java
public class Hello
```

---

# Advantages of Java

- Platform Independent
- Object Oriented
- Secure
- Portable
- Robust
- Multithreaded
- Distributed

---

# Applications of Java

- Android Apps
- Banking Systems
- Web Applications
- Desktop Applications
- Enterprise Software
- Scientific Applications

---

# Important Java Commands

| Command | Purpose |
|---|---|
| `java -version` | Check Java Version |
| `javac -version` | Check Compiler Version |
| `javac FileName.java` | Compile Java Program |
| `java ClassName` | Run Java Program |

---

<div align="center">

# Java Successfully Installed

Java Environment is now ready for:
- OOP Lab Programs
- Java Projects
- VS Code Development
- GitHub Repository Management

</div>