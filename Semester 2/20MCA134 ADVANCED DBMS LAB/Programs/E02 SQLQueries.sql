-- EXERCISE 2 : SQL QUERIES

-- 1. DISPLAY ALL COUNTRIES

SELECT country_name AS Countries
FROM countries;

-- 2. DISPLAY EMAIL AND PHONE NUMBER OF EMPLOYEES

SELECT email, phone_number
FROM employees;

-- 3. DISPLAY DATA OF EMPLOYEE WHOSE LAST NAME IS "FAY"

SELECT *
FROM employees
WHERE last_name = 'Fay';

-- 4. DISPLAY HIRE DATE OF EMPLOYEES WHOSE LAST NAME IS "GRANT" OR "WHALEN"

SELECT hire_date
FROM employees
WHERE last_name IN ('Grant','Whalen');

-- 5. DISPLAY NAME OF EMPLOYEE WHO IS SHIPPING CLERK

SELECT CONCAT(employees.first_name,' ',employees.last_name) AS Employee_Name,
jobs.job_id
FROM employees
INNER JOIN jobs
ON employees.job_id = jobs.job_id
WHERE jobs.job_title = 'Shipping Clerk';

-- 6. DISPLAY EMPLOYEES WHO WORK FOR DEPARTMENT 8

SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
department_id
FROM employees
WHERE department_id = '8';

-- 7. DISPLAY DEPARTMENTS IN DESCENDING ORDER

SELECT department_name
FROM dept
ORDER BY department_name DESC;

-- 8. DISPLAY EMPLOYEES WHOSE LAST NAME STARTS WITH "K"

SELECT CONCAT(first_name,' ',last_name) AS Employee_Name
FROM employees
WHERE last_name LIKE 'K%';

-- 9. DISPLAY EMPLOYEES HIRED BETWEEN 1995 AND 1997

SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
hire_date
FROM employees
WHERE YEAR(hire_date) BETWEEN 1995 AND 1997;

-- 10. DISPLAY JOBS WHERE MAXIMUM SALARY IS LESS THAN 5000

SELECT job_title
FROM jobs
WHERE max_salary <= 5000;

-- 11. DISPLAY EMAIL ADDRESS IN LOWER CASE

SELECT LOWER(email) AS Email
FROM employees;

-- 12. DISPLAY EMPLOYEES HIRED IN 1995

SELECT CONCAT(first_name,' ',last_name) AS Employee_Name
FROM employees
WHERE YEAR(hire_date) = 1995;

-- 13. INSERT EMPLOYEE "PAUL NEWTON" IN DEPARTMENT 11

INSERT INTO employees
(employee_id, first_name, last_name, email, phone_number,hire_date, job_id, salary, manager_id, department_id)
VALUES
(207,'Paul','Newton','paul.newton@sqltutorial.org','585.123.4567','1987-07-17',2,12000,101,11);

-- VERIFY INSERTION

SELECT *
FROM employees
WHERE employee_id = 207;

-- 14. DELETE SHIPPING DEPARTMENT

DELETE FROM employees
WHERE department_id = '5';

-- VERIFY EMPLOYEE DELETION

SELECT *
FROM employees
WHERE department_id = '5';

DELETE FROM dept
WHERE department_name = 'Shipping';

-- VERIFY DEPARTMENT DELETION

SELECT *
FROM dept
WHERE department_name = 'Shipping';

-- 15. DISPLAY EMPLOYEES HIRED ON THURSDAY

SELECT CONCAT(first_name,' ',last_name) AS Employee_Name,
hire_date
FROM employees
WHERE DAYNAME(hire_date) = 'Thursday';