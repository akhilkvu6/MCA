# Exercise 02 – SQL Queries

## Aim

To perform various SQL queries using SELECT, INSERT, DELETE, JOIN, ORDER BY, LIKE, and built-in MySQL functions on the Company Database.

---

# Theory

SQL (Structured Query Language) is used to communicate with relational databases for storing, retrieving, updating, and deleting data.

---

# SQL Clauses and Functions Used

| Clause / Function | Description |
|---|---|
| SELECT | Retrieves data from tables |
| WHERE | Filters records |
| ORDER BY | Sorts records |
| LIKE | Pattern matching |
| IN | Matches multiple values |
| INNER JOIN | Combines matching rows from tables |
| CONCAT() | Combines strings |
| LOWER() | Converts text to lowercase |
| YEAR() | Extracts year from date |
| DAYNAME() | Returns day name from date |
| INSERT | Adds records |
| DELETE | Removes records |

---

# Important Syntax

---

## 1. SELECT Statement

### Syntax

```sql
SELECT column_name
FROM table_name;
```

### Description

Used to retrieve records from a table.

### Example

```sql
SELECT * FROM employees;
```

---

## 2. WHERE Clause

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

### Description

Filters rows based on conditions.

### Example

```sql
SELECT *
FROM employees
WHERE last_name = 'Fay';
```

---

## 3. LIKE Operator

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name LIKE pattern;
```

### Description

Used for pattern matching.

### Variations

| Symbol | Meaning |
|---|---|
| % | Any number of characters |
| _ | Single character |

### Example

```sql
SELECT *
FROM employees
WHERE last_name LIKE 'K%';
```

---

## 4. IN Operator

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name IN(value1,value2);
```

### Description

Checks multiple values in a condition.

### Example

```sql
SELECT hire_date
FROM employees
WHERE last_name IN('Grant','Whalen');
```

---

## 5. ORDER BY Clause

### Syntax

```sql
SELECT column_name
FROM table_name
ORDER BY column_name DESC;
```

### Description

Sorts records in ascending or descending order.

### Example

```sql
SELECT department_name
FROM dept
ORDER BY department_name DESC;
```

---

## 6. INNER JOIN

### Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

### Description

Returns matching records from two tables.

### Example

```sql
SELECT employees.first_name, jobs.job_title
FROM employees
INNER JOIN jobs
ON employees.job_id = jobs.job_id;
```

---

## 7. CONCAT() Function

### Syntax

```sql
CONCAT(string1,string2)
```

### Description

Combines multiple strings into one string.

### Example

```sql
SELECT CONCAT(first_name,' ',last_name)
FROM employees;
```

---

## 8. LOWER() Function

### Syntax

```sql
LOWER(column_name)
```

### Description

Converts text into lowercase.

### Example

```sql
SELECT LOWER(email)
FROM employees;
```

---

## 9. YEAR() Function

### Syntax

```sql
YEAR(date_column)
```

### Description

Extracts year from a date.

### Example

```sql
SELECT *
FROM employees
WHERE YEAR(hire_date)=1995;
```

---

## 10. DAYNAME() Function

### Syntax

```sql
DAYNAME(date_column)
```

### Description

Returns the name of the day from a date.

### Example

```sql
SELECT *
FROM employees
WHERE DAYNAME(hire_date)='Thursday';
```

---

## 11. INSERT Statement

### Syntax

```sql
INSERT INTO table_name(columns)
VALUES(values);
```

### Description

Inserts new records into a table.

### Example

```sql
INSERT INTO employees(employee_id,first_name)
VALUES(207,'Paul');
```

---

## 12. DELETE Statement

### Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

### Description

Deletes records from a table.

### Example

```sql
DELETE FROM dept
WHERE department_name='Shipping';
```

---

# Program

## 1. Display All Countries

```sql
SELECT country_name AS Countries
FROM countries;
```

---

## 2. Display Email and Phone Number of Employees

```sql
SELECT email, phone_number
FROM employees;
```

---

## 3. Display Data of Employee Whose Last Name is "Fay"

```sql
SELECT *
FROM employees
WHERE last_name = 'Fay';
```

---

## 4. Display Hire Date of Employees Whose Last Name is "Grant" or "Whalen"

```sql
SELECT hire_date
FROM employees
WHERE last_name IN ('Grant','Whalen');
```

---

## 5. Display Name of Employee Who is Shipping Clerk

```sql
SELECT CONCAT(employees.first_name,' ',employees.last_name) AS Employee_Name,
jobs.job_id
FROM employees
INNER JOIN jobs
ON employees.job_id = jobs.job_id
WHERE jobs.job_title = 'Shipping Clerk';
```

---

## 6. Display Employees Who Work for Department 8

```sql
SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
department_id
FROM employees
WHERE department_id = '8';
```

---

## 7. Display Departments in Descending Order

```sql
SELECT department_name
FROM dept
ORDER BY department_name DESC;
```

---

## 8. Display Employees Whose Last Name Starts with "K"

```sql
SELECT CONCAT(first_name,' ',last_name) AS Employee_Name
FROM employees
WHERE last_name LIKE 'K%';
```

---

## 9. Display Employees Hired Between 1995 and 1997

```sql
SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
hire_date
FROM employees
WHERE YEAR(hire_date) BETWEEN 1995 AND 1997;
```

---

## 10. Display Jobs Where Maximum Salary is Less Than 5000

```sql
SELECT job_title
FROM jobs
WHERE max_salary <= 5000;
```

---

## 11. Display Email Address in Lower Case

```sql
SELECT LOWER(email) AS Email
FROM employees;
```

---

## 12. Display Employees Hired in 1995

```sql
SELECT CONCAT(first_name,' ',last_name) AS Employee_Name
FROM employees
WHERE YEAR(hire_date) = 1995;
```

---

## 13. Insert Employee "Paul Newton" in Department 11

```sql
DELETE FROM employees
WHERE employee_id = 207;

INSERT INTO employees
(employee_id, first_name, last_name, email, phone_number,
hire_date, job_id, salary, manager_id, department_id)

VALUES
(207,'Paul','Newton','paul.newton@sqltutorial.org',
'585.123.4567','1987-07-17',2,12000,101,11);

SELECT *
FROM employees
WHERE employee_id = 207;
```

---

## 14. Delete Shipping Department

```sql
DELETE FROM employees
WHERE department_id = '5';

SELECT *
FROM employees
WHERE department_id = '5';

DELETE FROM dept
WHERE department_name = 'Shipping';

SELECT *
FROM dept
WHERE department_name = 'Shipping';
```

---

## 15. Display Employees Hired on Thursday

```sql
SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
hire_date
FROM employees
WHERE DAYNAME(hire_date) = 'Thursday';
```

---

# Output

- SQL queries executed successfully.
- Required records were retrieved.
- Employee inserted successfully.
- Shipping department deleted successfully.
- Verification queries executed successfully.

---

# Advantages

- Fast data retrieval
- Easy data filtering
- Efficient sorting and searching
- Supports relational operations
- Easy database management

---

# Applications

- Employee management systems
- Banking systems
- Inventory management
- College management systems
- Enterprise database applications

---

# Conclusion

Successfully executed various SQL queries using SELECT, WHERE, ORDER BY, JOIN, INSERT, DELETE, and MySQL built-in functions on the Company Database.

---

# Viva Questions

1. What is SQL?
2. Difference between DDL and DML.
3. What is the purpose of WHERE clause?
4. Explain LIKE operator.
5. Difference between DELETE and DROP.
6. What is INNER JOIN?
7. Explain CONCAT() function.
8. What is the use of LOWER()?
9. Explain YEAR() function.
10. Explain DAYNAME() function.
11. Difference between PRIMARY KEY and FOREIGN KEY.
12. What is pattern matching in SQL?
13. Explain ORDER BY clause.
14. What is the use of IN operator?
15. What is normalization?