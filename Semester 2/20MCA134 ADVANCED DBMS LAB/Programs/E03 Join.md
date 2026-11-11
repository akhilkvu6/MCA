# Exercise 03 – Join

## Aim

To perform SQL JOIN operations and database manipulation queries on the UNIVERSITY database using MySQL.

---

# Theory

JOIN operations are used to combine rows from two or more tables based on related columns.

SQL joins help retrieve meaningful information stored across multiple relational tables.

---

# Types of SQL Operations Used

| Operation | Description |
|---|---|
| CREATE DATABASE | Creates database |
| CREATE TABLE | Creates tables |
| INSERT | Inserts records |
| SELECT | Retrieves records |
| INNER JOIN | Combines matching rows |
| UPDATE | Updates records |
| DELETE | Deletes records |
| VIEW | Creates virtual table |
| GROUP BY | Groups records |
| COUNT() | Counts rows |

---

# Tables Used

| Table Name | Purpose |
|---|---|
| STUDENT | Stores student details |
| COURSE | Stores course details |
| SECTION | Stores section details |
| GRADE_REPORT | Stores grades |
| PREREQUISITE | Stores prerequisite details |

---

# Important SQL Syntax

---

## 1. CREATE DATABASE

### Syntax

```sql
CREATE DATABASE database_name;
```

### Example

```sql
CREATE DATABASE UNIVERSITY;
```

---

## 2. CREATE TABLE

### Syntax

```sql
CREATE TABLE table_name
(
    column_name datatype constraints
);
```

### Description

Creates a table with specified columns and constraints.

---

## 3. PRIMARY KEY

### Syntax

```sql
column_name datatype PRIMARY KEY
```

### Description

Uniquely identifies each row in a table.

---

## 4. FOREIGN KEY

### Syntax

```sql
FOREIGN KEY(column_name)
REFERENCES parent_table(parent_column)
```

### Description

Creates relationship between tables.

---

## 5. INSERT INTO

### Syntax

```sql
INSERT INTO table_name
VALUES(values);
```

### Description

Inserts records into tables.

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

Returns matching records from multiple tables.

---

## 7. VIEW

### Syntax

```sql
CREATE VIEW view_name AS
SELECT statement;
```

### Description

Creates a virtual table.

---

## 8. UPDATE

### Syntax

```sql
UPDATE table_name
SET column_name = value
WHERE condition;
```

### Description

Updates existing records.

---

## 9. DELETE

### Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

### Description

Deletes records from table.

---

## 10. GROUP BY

### Syntax

```sql
GROUP BY column_name;
```

### Description

Groups rows having same values.

---

## 11. COUNT()

### Syntax

```sql
COUNT(column_name)
```

### Description

Returns number of rows.

---

# Program

## 1. Create UNIVERSITY Database

```sql
CREATE DATABASE UNIVERSITY;

USE UNIVERSITY;
```

---

## Create STUDENT Table

```sql
CREATE TABLE STUDENT
(
    Name VARCHAR(10),
    Student_number INT PRIMARY KEY,
    Class INT,
    Major VARCHAR(20)
);
```

---

## Create COURSE Table

```sql
CREATE TABLE COURSE
(
    Course_name VARCHAR(30),
    Course_number VARCHAR(20) PRIMARY KEY,
    Credit_hours INT,
    Department VARCHAR(15)
);
```

---

## Create SECTION Table

```sql
CREATE TABLE SECTION
(
    Section_identifier INT PRIMARY KEY,
    Course_number VARCHAR(20),
    Semester VARCHAR(10),
    Year_Of_Course INT,
    Instructor VARCHAR(15),

    FOREIGN KEY (Course_number)
    REFERENCES COURSE(Course_number)
);
```

---

## Create GRADE_REPORT Table

```sql
CREATE TABLE GRADE_REPORT
(
    Student_number INT,
    Section_identifier INT,
    Grade VARCHAR(2),

    FOREIGN KEY (Student_number)
    REFERENCES STUDENT(Student_number),

    FOREIGN KEY (Section_identifier)
    REFERENCES SECTION(Section_identifier),

    PRIMARY KEY (Student_number,Section_identifier)
);
```

---

## Create PREREQUISITE Table

```sql
CREATE TABLE PREREQUISITE
(
    Course_number VARCHAR(20),
    Prerequisite_number VARCHAR(20),

    FOREIGN KEY (Course_number)
    REFERENCES COURSE(Course_number),

    FOREIGN KEY (Prerequisite_number)
    REFERENCES COURSE(Course_number),

    PRIMARY KEY (Course_number,Prerequisite_number)
);
```

---

# Insert Queries

## Insert into STUDENT

```sql
INSERT INTO STUDENT
VALUES
('Smith',17,1,'CS'),
('Brown',8,2,'CS');
```

---

## Insert into COURSE

```sql
INSERT INTO COURSE
VALUES
('Intro to Computer Science','CS1310',4,'CS'),
('Data Structures','CS3320',4,'CS'),
('Discrete Mathematics','MATH2410',3,'MATH'),
('Database','CS3380',3,'CS');
```

---

## Insert into SECTION

```sql
INSERT INTO SECTION
VALUES
(85,'MATH2410','Fall',2007,'King'),
(92,'CS1310','Fall',2007,'Anderson'),
(102,'CS3320','Spring',2008,'Knuth'),
(112,'MATH2410','Fall',2008,'Chang'),
(119,'CS1310','Fall',2008,'Anderson'),
(135,'CS3380','Fall',2008,'Stone');
```

---

## Insert into GRADE_REPORT

```sql
INSERT INTO GRADE_REPORT
VALUES
(17,112,'B'),
(17,119,'C'),
(8,85,'A'),
(8,92,'A'),
(8,102,'B'),
(8,135,'A');
```

---

## Insert into PREREQUISITE

```sql
INSERT INTO PREREQUISITE
VALUES
('CS3380','CS3320'),
('CS3380','MATH2410'),
('CS3320','CS1310');
```

---

# SQL Queries

## 3. Retrieve Courses and Grades of Smith

```sql
SELECT c.Course_name,
g.Grade
FROM STUDENT s
INNER JOIN GRADE_REPORT g
ON s.Student_number = g.Student_number
INNER JOIN SECTION se
ON g.Section_identifier = se.Section_identifier
INNER JOIN COURSE c
ON se.Course_number = c.Course_number
WHERE s.Name = 'Smith';
```

---

## 4. List Students Who Took Database Course in Fall 2008

```sql
SELECT s.Name,
g.Grade
FROM STUDENT s
INNER JOIN GRADE_REPORT g
ON s.Student_number = g.Student_number
INNER JOIN SECTION se
ON g.Section_identifier = se.Section_identifier
INNER JOIN COURSE c
ON se.Course_number = c.Course_number
WHERE c.Course_name = 'Database'
AND se.Semester = 'Fall'
AND se.Year_Of_Course = 2008;
```

---

## 5. List Prerequisites of Database Course

```sql
SELECT Course_name
FROM COURSE
WHERE Course_number IN
(
    SELECT p.Prerequisite_number
    FROM PREREQUISITE p
    JOIN COURSE c
    ON p.Course_number = c.Course_number
    WHERE p.Course_number =
    (
        SELECT Course_number
        FROM COURSE
        WHERE Course_name = 'Database'
    )
);
```

---

## 6. Create View for Senior CS Students

```sql
CREATE VIEW seniors AS
SELECT *
FROM STUDENT
WHERE Class = 2
AND Major = 'CS';

SELECT Name
FROM seniors;
```

---

## 7. Retrieve Courses Taught by Professor King

```sql
SELECT c.Course_name
FROM COURSE c
JOIN SECTION s
ON c.Course_number = s.Course_number
WHERE s.Instructor = 'King'
AND s.Year_Of_Course IN (2007,2008);
```

---

## 8. Retrieve Section Details and Number of Students

```sql
SELECT s.Course_number,
s.Semester,
s.Year_Of_Course,
COUNT(g.Student_number) AS No_of_students
FROM SECTION s
JOIN GRADE_REPORT g
ON s.Section_identifier = g.Section_identifier
WHERE s.Instructor = 'King'
GROUP BY s.Course_number,
s.Semester,
s.Year_Of_Course,
g.Section_identifier;
```

---

## 9. Retrieve Transcript of Senior CS Students

```sql
SELECT s.Name,
c.Course_name,
c.Course_number,
c.Credit_hours,
se.Semester,
se.Year_Of_Course,
g.Grade
FROM STUDENT s
JOIN GRADE_REPORT g
ON s.Student_number = g.Student_number
JOIN SECTION se
ON g.Section_identifier = se.Section_identifier
JOIN COURSE c
ON se.Course_number = c.Course_number
WHERE s.Class = 2
AND s.Major = 'CS';
```

---

## 10(a). Insert New Student

```sql
INSERT INTO STUDENT
VALUES
('Johnson',25,1,'Math');

SELECT *
FROM STUDENT
WHERE Student_number = 25;
```

---

## 10(b). Update Class of Smith

```sql
UPDATE STUDENT
SET Class = 2
WHERE Name = 'Smith';

SELECT *
FROM STUDENT
WHERE Name = 'Smith';
```

---

## 10(c). Insert New Course

```sql
INSERT INTO COURSE
VALUES
('Knowledge Engineering','CS4390',3,'CS');

SELECT *
FROM COURSE
WHERE Course_number = 'CS4390';
```

---

## 10(d). Delete Student Smith

```sql
DELETE FROM GRADE_REPORT
WHERE Student_number = 17;

DELETE FROM STUDENT
WHERE Name = 'Smith'
AND Student_number = 17;

SELECT *
FROM STUDENT;
```

---

# Output

- Database created successfully.
- Tables created successfully.
- Records inserted successfully.
- JOIN queries executed successfully.
- View created successfully.
- UPDATE and DELETE operations completed successfully.

---

# Advantages

- Efficient retrieval of related data
- Reduces data redundancy
- Supports relational database management
- Easy data manipulation
- Maintains referential integrity

---

# Applications

- University management systems
- Student information systems
- Examination management
- ERP systems
- Relational database applications

---

# Conclusion

Successfully implemented JOIN operations and SQL queries on the UNIVERSITY database using MySQL.

---

# Viva Questions

1. What is JOIN?
2. Difference between INNER JOIN and OUTER JOIN.
3. What is a VIEW?
4. What is GROUP BY?
5. Explain COUNT() function.
6. What is a PRIMARY KEY?
7. What is a FOREIGN KEY?
8. Difference between DELETE and DROP.
9. What is referential integrity?
10. Explain UPDATE statement.
11. Explain nested queries.
12. What is normalization?
13. What is SQL?
14. Difference between CHAR and VARCHAR.
15. Explain relational database.