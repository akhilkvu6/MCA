<div align="center">

# MySQL Workbench Installation Guide

## Windows Setup for MySQL Development

</div>

---

# Introduction

MySQL Workbench is a graphical tool used for:

* Writing SQL queries
* Creating databases and tables
* Managing MySQL servers
* Executing SQL scripts
* Database administration
* Data modeling

MySQL Workbench works together with MySQL Server.

---

# Requirements

Before installing MySQL Workbench, ensure:

* Windows 10 / Windows 11
* Internet Connection
* Administrator Access

---

# Software Required

| Software        | Purpose                   |
| --------------- | ------------------------- |
| MySQL Server    | Database Server           |
| MySQL Workbench | GUI Tool for MySQL        |
| MySQL Installer | Installs MySQL Components |

---

# Step 1 - Download MySQL Installer

Open browser and visit:

```text id="e5oq4r"
https://dev.mysql.com/downloads/installer/
```

Download:

```text id="r3y1pz"
Windows (x86, 32-bit), MSI Installer
```

Recommended:

```text id="4zj2xv"
MySQL Installer Community Edition
```

---

# Step 2 - Run MySQL Installer

1. Open downloaded installer file.

Example:

```text id="n0x9x4"
mysql-installer-community-8.0.xx.msi
```

2. Click:

```text id="zj7m0q"
Yes
```

for administrator permission.

3. MySQL Installer window opens.

---

# Step 3 - Choose Setup Type

Select:

```text id="g6j8w5"
Developer Default
```

This installs:

* MySQL Server
* MySQL Workbench
* MySQL Shell
* Connectors
* Documentation

Click:

```text id="d9v2kk"
Next
```

---

# Step 4 - Install Required Dependencies

If prompted:

* Install Visual C++ Redistributable
* Install additional required packages

Click:

```text id="m0y6qz"
Execute
```

Then click:

```text id="z3y1lv"
Next
```

---

# Step 5 - Install MySQL Products

1. Review selected products.
2. Click:

```text id="5xk6yv"
Execute
```

3. Wait for installation to complete.
4. Click:

```text id="j5g2wp"
Next
```

---

# Step 6 - Configure MySQL Server

## Configuration Type

Select:

```text id="v4m0xz"
Development Computer
```

---

## Connectivity

Keep default port:

```text id="e7r6qv"
3306
```

---

## Authentication Method

Select:

```text id="n7v4xj"
Use Strong Password Encryption
```

Click:

```text id="5r4n1z"
Next
```

---

# Step 7 - Create Root Password

Set root password.

Example:

```text id="2qv5ok"
root123
```

Use a strong password for security.

Click:

```text id="8r9xw0"
Next
```

---

# Step 8 - Configure Windows Service

Keep default settings:

| Setting                 | Value   |
| ----------------------- | ------- |
| Windows Service Name    | MySQL80 |
| Start at System Startup | Enabled |

Click:

```text id="k5v9n4"
Next
```

---

# Step 9 - Apply Configuration

1. Click:

```text id="w8v2xg"
Execute
```

2. Wait for configuration process.
3. Click:

```text id="y7n4oz"
Finish
```

---

# Step 10 - Launch MySQL Workbench

Open:

```text id="0r3z4m"
MySQL Workbench
```

from Start Menu.

---

# Step 11 - Connect to MySQL Server

1. Click:

```text id="q8x5rm"
Local instance MySQL80
```

2. Enter root password.
3. Click:

```text id="v6m4jx"
OK
```

MySQL Workbench dashboard opens successfully.

---

# MySQL Workbench Interface

| Component    | Purpose                |
| ------------ | ---------------------- |
| Navigator    | Database objects       |
| SQL Editor   | Execute SQL queries    |
| Output Panel | Displays query results |
| Schemas      | Displays databases     |

---

# Creating Database

```sql id="4y7o2m"
CREATE DATABASE college;
```

---

# Selecting Database

```sql id="1r7x9p"
USE college;
```

---

# Creating Table

```sql id="r4o7g5"
CREATE TABLE Student
(
    id INT PRIMARY KEY,
    name VARCHAR(30)
);
```

---

# Inserting Data

```sql id="8n3m1j"
INSERT INTO Student
VALUES
(1, 'Akhil');
```

---

# Viewing Data

```sql id="4w9v5x"
SELECT * FROM Student;
```

---

# Verify MySQL Installation

Open Command Prompt and run:

```bash id="6y8q1o"
mysql --version
```

Expected Output:

```text id="2v0r8m"
mysql  Ver 8.0.xx for Win64
```

---

# Start MySQL Service

```bash id="x9k2j7"
net start MySQL80
```

---

# Stop MySQL Service

```bash id="l0m6xw"
net stop MySQL80
```

---

# Recommended Folder Structure

```text id="7m1r2v"
MCA/
│
├── Semester 2/
│   ├── 20MCA134 ADVANCED DBMS LAB/
│   │
│   │   ├── Installation/
│   │   │   └── MySQL_Workbench_Installation.md
│   │   │
│   │   ├── SQL/
│   │   ├── mongoDB/
│   │   └── README.md
```

---

# Common Errors and Solutions

## 1. Cannot Connect to MySQL Server

### Reason

MySQL service is not running.

### Solution

Start MySQL service:

```bash id="n4w8g6"
net start MySQL80
```

---

## 2. Access Denied for User 'root'

### Reason

Incorrect password.

### Solution

Use correct root password created during installation.

---

## 3. Port 3306 Already in Use

### Reason

Another application is using MySQL port.

### Solution

Change port number during configuration.

---

## 4. MySQL Command Not Recognized

### Reason

PATH variable not configured.

### Solution

Add MySQL bin directory to PATH.

Example:

```text id="5j7v0w"
C:\Program Files\MySQL\MySQL Server 8.0\bin
```

---

# Advantages of MySQL Workbench

* Easy graphical interface
* SQL editor with syntax highlighting
* Database visualization
* Query execution support
* Import and export support
* Database administration tools

---

# Applications of MySQL Workbench

* Database development
* SQL query execution
* Database administration
* Data modeling
* Academic lab work
* Backend application development

---

# Important MySQL Commands

| Command                    | Purpose             |
| -------------------------- | ------------------- |
| `mysql --version`          | Check MySQL Version |
| `net start MySQL80`        | Start MySQL Service |
| `net stop MySQL80`         | Stop MySQL Service  |
| `CREATE DATABASE`          | Create Database     |
| `USE database_name`        | Select Database     |
| `SELECT * FROM table_name` | Display Table Data  |

---

# Internal Working

1. MySQL Server runs as a background service
2. MySQL Workbench connects to server
3. SQL queries are sent to MySQL Server
4. Server processes queries
5. Results are returned to Workbench

---

# Viva Questions and Answers

## 1. What is MySQL Workbench?

MySQL Workbench is a graphical tool used to manage MySQL databases.

---

## 2. What is MySQL Server?

MySQL Server is the database engine that stores and manages databases.

---

## 3. Difference between MySQL Server and MySQL Workbench?

| MySQL Server    | MySQL Workbench              |
| --------------- | ---------------------------- |
| Database engine | GUI management tool          |
| Stores data     | Used to interact with server |

---

## 4. What is port 3306?

3306 is the default port used by MySQL Server.

---

## 5. What is root user?

Root is the default administrator account in MySQL.

---

## 6. What is SQL?

SQL stands for Structured Query Language used for database operations.

---

## 7. What is a schema?

Schema is another name for database in MySQL.

---

## 8. What is the use of Workbench?

Workbench is used to visually manage databases and execute SQL queries.

---

## 9. What is the use of `USE` command?

`USE` selects a database.

Example:

```sql id="z0w5m2"
USE college;
```

---

## 10. What is Primary Key?

Primary Key uniquely identifies each row in a table.

---

<div align="center">

# MySQL Workbench Successfully Installed

MySQL Environment is now ready for:

* Advanced DBMS Lab
* SQL Programming
* Trigger Programs
* Stored Procedures
* MongoDB and Database Projects

</div>
