# Exercise 01 – Company Database

## Aim

To design and create a Company Database using MySQL and perform DDL and DML operations such as table creation, table modification, and data insertion.

---

# Theory

## What is DBMS?

A Database Management System (DBMS) is software used to create, manage, store, and manipulate databases efficiently.

Examples:
- MySQL
- Oracle
- PostgreSQL
- MongoDB

---

# DDL Commands

DDL (Data Definition Language) commands are used to define and modify database structures.

## Common DDL Commands

| Command | Description |
|---|---|
| CREATE | Creates database or table |
| ALTER | Modifies structure of table |
| DROP | Deletes database or table |
| TRUNCATE | Removes all rows from table |
| RENAME | Renames database objects |

---

# DML Commands

DML (Data Manipulation Language) commands are used to manipulate data stored inside tables.

## Common DML Commands

| Command | Description |
|---|---|
| INSERT | Inserts records |
| UPDATE | Updates records |
| DELETE | Deletes records |
| SELECT | Retrieves records |

---

# Database Used

Database Name:

```sql
company
```

---

# Tables Used

The company database contains seven tables.

| Table Name | Purpose |
|---|---|
| employees | Stores employee details |
| jobs | Stores job details |
| departments | Stores department details |
| dependents | Stores employee dependents |
| locations | Stores department locations |
| countries | Stores country information |
| regions | Stores region information |

---

# Important SQL Syntax Used

---

## 1. CREATE DATABASE

### Syntax

```sql
CREATE DATABASE database_name;
```

### Description

Creates a new database in MySQL.

### Example

```sql
CREATE DATABASE company;
```

---

## 2. USE DATABASE

### Syntax

```sql
USE database_name;
```

### Description

Selects the database for performing operations.

### Example

```sql
USE company;
```

---

## 3. CREATE TABLE

### Syntax

```sql
CREATE TABLE table_name
(
    column_name datatype constraints
);
```

### Description

Creates a new table with specified columns and constraints.

### Variations

#### With Primary Key

```sql
CREATE TABLE student
(
    id INT PRIMARY KEY,
    name VARCHAR(20)
);
```

#### With Foreign Key

```sql
CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,

    FOREIGN KEY(customer_id)
    REFERENCES customer(id)
);
```

---

## 4. PRIMARY KEY

### Syntax

```sql
column_name datatype PRIMARY KEY
```

### Description

A primary key uniquely identifies each row in a table.

### Properties

- Unique
- Cannot contain NULL values
- Only one primary key per table

---

## 5. FOREIGN KEY

### Syntax

```sql
FOREIGN KEY(column_name)
REFERENCES parent_table(parent_column)
```

### Description

Creates a relationship between two tables.

### Purpose

Maintains referential integrity.

---

## 6. ALTER TABLE

### Syntax

```sql
ALTER TABLE table_name operation;
```

### Description

Used to modify an existing table structure.

### Variations

#### Rename Table

```sql
ALTER TABLE departments
RENAME TO dept;
```

#### Modify Column

```sql
ALTER TABLE employees
MODIFY COLUMN salary SMALLINT;
```

#### Add Column

```sql
ALTER TABLE employees
ADD commission VARCHAR(50);
```

---

## 7. INSERT INTO

### Syntax

```sql
INSERT INTO table_name(column1,column2)
VALUES(value1,value2);
```

### Description

Inserts records into a table.

### Variations

#### Single Row Insert

```sql
INSERT INTO student(id,name)
VALUES(1,'Akhil');
```

#### Multiple Row Insert

```sql
INSERT INTO student(id,name)
VALUES
(1,'Akhil'),
(2,'Arun');
```

---

## 8. SELECT

### Syntax

```sql
SELECT * FROM table_name;
```

### Description

Retrieves records from a table.

---

## 9. DESC / DESCRIBE

### Syntax

```sql
DESC table_name;
```

### Description

Displays the structure of a table.

---

# Program

## Create Database

```sql
CREATE DATABASE company;

USE company;
```

---

## Create jobs Table

```sql
CREATE TABLE jobs
(
    job_id VARCHAR(10) PRIMARY KEY,
    job_title VARCHAR(50),
    min_salary DOUBLE,
    max_salary DOUBLE
);
```

---

## Create regions Table

```sql
CREATE TABLE regions
(
    region_id VARCHAR(10) PRIMARY KEY,
    region_name VARCHAR(50)
);
```

---

## Create countries Table

```sql
CREATE TABLE countries
(
    country_id VARCHAR(10) PRIMARY KEY,
    country_name VARCHAR(50),
    region_id VARCHAR(10),

    FOREIGN KEY(region_id)
    REFERENCES regions(region_id)
);
```

---

## Create locations Table

```sql
CREATE TABLE locations
(
    location_id VARCHAR(10) PRIMARY KEY,
    street_address VARCHAR(50),
    postal_code VARCHAR(50),
    city VARCHAR(50),
    state_province VARCHAR(50),
    country_id VARCHAR(10),

    FOREIGN KEY(country_id)
    REFERENCES countries(country_id)
);
```

---

## Create departments Table

```sql
CREATE TABLE departments
(
    department_id VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(50),
    location_id VARCHAR(10),

    FOREIGN KEY(location_id)
    REFERENCES locations(location_id)
);
```

---

## Create employees Table

```sql
CREATE TABLE employees
(
    employee_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(50),
    hire_date DATE,
    job_id VARCHAR(10),
    salary DOUBLE,
    manager_id VARCHAR(10),
    department_id VARCHAR(10),

    FOREIGN KEY(department_id)
    REFERENCES departments(department_id),

    FOREIGN KEY(job_id)
    REFERENCES jobs(job_id),

    FOREIGN KEY(manager_id)
    REFERENCES employees(employee_id)
);
```

---

## Create dependents Table

```sql
CREATE TABLE dependents
(
    dependent_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    relationship VARCHAR(50),
    employee_id VARCHAR(10),

    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);
```

---

# ALTER TABLE Operations

## Rename departments Table

```sql
ALTER TABLE departments
RENAME TO dept;
```

### Verification

```sql
DESC dept;
```

---

## Modify salary Column

```sql
ALTER TABLE employees
MODIFY COLUMN salary SMALLINT;
```

### Verification

```sql
DESC employees;
```

---

## Add commission Column

```sql
ALTER TABLE employees
ADD commission VARCHAR(50);
```

### Verification

```sql
DESC employees;
```

---

# Insert Queries

## Insert into regions

```sql
INSERT INTO regions(region_id, region_name)
VALUES
('1','Europe'),
('2','Americas'),
('3','Asia'),
('4','Middle East and Africa');
```

---

## Insert into countries

```sql
INSERT INTO countries(country_id, country_name, region_id)
VALUES
('AR','Argentina','2'),
('AU','Australia','3'),
('BE','Belgium','1');
```

---

## Insert into locations

```sql
INSERT INTO locations
(location_id, street_address, postal_code, city, state_province, country_id)
VALUES
('1400','2014 Jabberwocky Rd','26192','Southlake','Texas','US');
```

---

## Insert into jobs

```sql
INSERT INTO jobs(job_id, job_title, min_salary, max_salary)
VALUES
('1','Public Accountant',4200,9000);
```

---

## Insert into departments

```sql
INSERT INTO departments(department_id, department_name, location_id)
VALUES
('1','Administration','1700');
```

---

## Insert into employees

```sql
INSERT INTO employees
(employee_id, first_name, last_name, email, phone_number,
hire_date, job_id, salary, manager_id, department_id)
VALUES
(100,'Steven','King','steven.king@sqltutorial.org',
'515.123.4567','1987-06-17',4,24000,NULL,9);
```

---

## Insert into dependents

```sql
INSERT INTO dependents
(dependent_id, first_name, last_name, relationship, employee_id)
VALUES
(1,'Penelope','Gietz','Child',206);
```

---

# Verification Queries

```sql
SHOW TABLES;

SELECT * FROM regions;
SELECT * FROM countries;
SELECT * FROM locations;
SELECT * FROM jobs;
SELECT * FROM dept;
SELECT * FROM employees;
SELECT * FROM dependents;
```

---

# Output

- Database created successfully.
- Tables created successfully.
- Records inserted successfully.
- Table modifications executed successfully.
- Queries verified successfully.

---

# Advantages

- Easy data management
- Maintains data integrity
- Supports relationships between tables
- Reduces data redundancy
- Efficient data retrieval

---

# Applications

- Employee management systems
- Banking systems
- Inventory systems
- College management systems
- Enterprise applications

---

# Conclusion

Successfully created and manipulated a Company Database using MySQL DDL and DML commands. Implemented table relationships using primary and foreign keys and performed data insertion and table modification operations.

---

# Viva Questions

1. What is DBMS?
2. What is MySQL?
3. What is DDL?
4. What is DML?
5. Difference between CHAR and VARCHAR.
6. What is a Primary Key?
7. What is a Foreign Key?
8. What is referential integrity?
9. Difference between DELETE, DROP and TRUNCATE.
10. What is normalization?
11. What is the purpose of ALTER TABLE?
12. Why are constraints used?
13. Difference between PRIMARY KEY and UNIQUE KEY.
14. What is SQL?
15. Explain CREATE TABLE syntax.

