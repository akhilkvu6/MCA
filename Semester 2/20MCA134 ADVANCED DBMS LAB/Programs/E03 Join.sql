-- EXERCISE 3 : JOIN

-- 1. CREATE UNIVERSITY DATABASE

CREATE DATABASE UNIVERSITY;

USE UNIVERSITY;

-- CREATE TABLE : STUDENT

CREATE TABLE STUDENT
(
    Name VARCHAR(10),
    Student_number INT PRIMARY KEY,
    Class INT,
    Major VARCHAR(20)
);

-- CREATE TABLE : COURSE

CREATE TABLE COURSE
(
    Course_name VARCHAR(30),
    Course_number VARCHAR(20) PRIMARY KEY,
    Credit_hours INT,
    Department VARCHAR(15)
);

-- CREATE TABLE : SECTION

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

-- CREATE TABLE : GRADE_REPORT

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

-- CREATE TABLE : PREREQUISITE

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

-- 2. INSERT VALUES INTO TABLES

-- INSERT INTO STUDENT

INSERT INTO STUDENT
VALUES
('Smith',17,1,'CS'),
('Brown',8,2,'CS');

-- VERIFY

SELECT *
FROM STUDENT;

-- INSERT INTO COURSE

INSERT INTO COURSE
VALUES
('Intro to Computer Science','CS1310',4,'CS'),
('Data Structures','CS3320',4,'CS'),
('Discrete Mathematics','MATH2410',3,'MATH'),
('Database','CS3380',3,'CS');

-- VERIFY

SELECT *
FROM COURSE;

-- INSERT INTO SECTION

INSERT INTO SECTION
VALUES
(85,'MATH2410','Fall',2007,'King'),
(92,'CS1310','Fall',2007,'Anderson'),
(102,'CS3320','Spring',2008,'Knuth'),
(112,'MATH2410','Fall',2008,'Chang'),
(119,'CS1310','Fall',2008,'Anderson'),
(135,'CS3380','Fall',2008,'Stone');

-- VERIFY

SELECT *
FROM SECTION;

-- INSERT INTO GRADE_REPORT

INSERT INTO GRADE_REPORT
VALUES
(17,112,'B'),
(17,119,'C'),
(8,85,'A'),
(8,92,'A'),
(8,102,'B'),
(8,135,'A');

-- VERIFY

SELECT *
FROM GRADE_REPORT;

-- INSERT INTO PREREQUISITE

INSERT INTO PREREQUISITE
VALUES
('CS3380','CS3320'),
('CS3380','MATH2410'),
('CS3320','CS1310');

-- VERIFY

SELECT *
FROM PREREQUISITE;

-- 3. LIST ALL COURSES AND GRADES OF "SMITH"

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

-- 4. LIST STUDENTS WHO TOOK DATABASE COURSE IN FALL 2008 AND THEIR GRADES

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

-- 5. LIST PREREQUISITES OF DATABASE COURSE

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

-- 6. CREATE VIEW FOR SENIOR STUDENTS MAJORING IN CS

CREATE VIEW seniors AS
SELECT *
FROM STUDENT
WHERE Class = 2
AND Major = 'CS';

SELECT Name
FROM seniors;

-- 7. RETRIEVE COURSES TAUGHT BY PROFESSOR KING IN 2007 AND 2008

SELECT c.Course_name
FROM COURSE c
JOIN SECTION s
ON c.Course_number = s.Course_number
WHERE s.Instructor = 'King'
AND s.Year_Of_Course IN (2007,2008);

-- 8. RETRIEVE SECTION DETAILS AND NUMBER OF STUDENTS TAUGHT BY KING

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

-- 9. RETRIEVE TRANSCRIPT OF SENIOR CS STUDENTS

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

-- 10(a). INSERT NEW STUDENT

DELETE FROM STUDENT
WHERE Student_number = 25;

INSERT INTO STUDENT
VALUES
('Johnson',25,1,'Math');

-- VERIFY

SELECT *
FROM STUDENT
WHERE Student_number = 25;

-- 10(b). CHANGE CLASS OF SMITH TO 2

UPDATE STUDENT
SET Class = 2
WHERE Name = 'Smith';

-- VERIFY

SELECT *
FROM STUDENT
WHERE Name = 'Smith';

-- 10(c). INSERT NEW COURSE

DELETE FROM COURSE
WHERE Course_number = 'CS4390';

INSERT INTO COURSE
VALUES
('Knowledge Engineering','CS4390',3,'CS');

-- VERIFY

SELECT *
FROM COURSE
WHERE Course_number = 'CS4390';

-- 10(d). DELETE STUDENT SMITH

DELETE FROM GRADE_REPORT
WHERE Student_number = 17;

DELETE FROM STUDENT
WHERE Name = 'Smith'
AND Student_number = 17;

-- VERIFY

SELECT *
FROM STUDENT;