# Exercise 04 – PLSQL Procedures

## Aim

To study and implement PL/SQL concepts in MySQL using Stored Procedures, variables, conditions, loops, and procedural database programming.

---

# Theory

PL/SQL (Procedural Language/Structured Query Language) is Oracle’s procedural extension of SQL.

MySQL does not directly support Oracle PL/SQL syntax. Instead, MySQL supports procedural programming using:
- Stored Procedures
- Functions
- Triggers
- Cursors
- Conditional Statements
- Loops

These are collectively used as PL/SQL concepts in MySQL.

PL/SQL allows combining SQL queries with procedural programming constructs such as variables, loops, and conditions.

---

# Stored Procedure

A Stored Procedure is a precompiled collection of SQL statements stored inside the database.

Stored procedures:
- improve performance,
- reduce code duplication,
- provide modular programming,
- and simplify database operations.

---

# Features of PL/SQL

- Combines SQL with procedural programming
- Supports variables and conditions
- Supports loops and branching
- Supports modular programming
- Provides faster execution
- Reduces network traffic
- Supports reusable code

---

# Components Used in PL/SQL

| Component | Description |
|---|---|
| DECLARE | Declares variables |
| SET | Assigns values |
| IF ELSE | Conditional statement |
| WHILE | Loop statement |
| PROCEDURE | Stored program |
| CALL | Executes procedure |
| DELIMITER | Changes statement terminator |

---

# DELIMITER

## Purpose

MySQL uses semicolon `;` as default statement terminator.

For stored procedures, delimiter is temporarily changed using:

```sql
DELIMITER //
```

After procedure creation:

```sql
DELIMITER ;
```

restores the default delimiter.

---

# General Syntax of Stored Procedure

```sql
DELIMITER //

CREATE PROCEDURE procedure_name(parameters)
BEGIN

    -- SQL statements

END //

DELIMITER ;
```

---

# Variable Declaration

## Syntax

```sql
DECLARE variable_name datatype;
```

## Example

```sql
DECLARE num INT;
```

---

# Assignment Statement

## Syntax

```sql
SET variable_name = value;
```

---

# IF ELSE Statement

## Syntax

```sql
IF condition THEN

    statements;

ELSE

    statements;

END IF;
```

---

# WHILE Loop

## Syntax

```sql
WHILE condition DO

    statements;

END WHILE;
```

---

# Program 1 – Procedure to Check Even or Odd

## Procedure

```sql
DROP PROCEDURE IF EXISTS even_odd;

DELIMITER //

CREATE PROCEDURE even_odd(IN num INT)
BEGIN

    DECLARE r VARCHAR(10);

    IF num % 2 = 0 THEN

        SET r = 'Even';

    ELSE

        SET r = 'Odd';

    END IF;

    SELECT num AS Number,
    r AS Result;

END //

DELIMITER ;
```

## SQL Query

```sql
CALL even_odd(7);
```

---

# Program 2 – Procedure to Display Grade for a Mark

## Procedure

```sql
DROP PROCEDURE IF EXISTS grade;

DELIMITER //

CREATE PROCEDURE grade(IN g INT)
BEGIN

    DECLARE des VARCHAR(50);

    IF g > 90 THEN

        SET des = 'Grade is A';

    ELSEIF g > 80 THEN

        SET des = 'Grade is B';

    ELSEIF g > 70 THEN

        SET des = 'Grade is C';

    ELSEIF g > 60 THEN

        SET des = 'Grade is D';

    ELSE

        SET des = 'Grade is E';

    END IF;

    SELECT g AS Marks,
    des AS Grade;

END //

DELIMITER ;
```

## SQL Query

```sql
CALL grade(87);
```

---

# Program 3 – Procedure to Check Positive, Negative or Zero

## Procedure

```sql
DROP PROCEDURE IF EXISTS pos_neg_zero;

DELIMITER //

CREATE PROCEDURE pos_neg_zero(IN num INT)
BEGIN

    DECLARE r VARCHAR(10);

    IF num > 0 THEN

        SET r = 'Positive';

    ELSEIF num < 0 THEN

        SET r = 'Negative';

    ELSE

        SET r = 'Zero';

    END IF;

    SELECT num AS Number,
    r AS Result;

END //

DELIMITER ;
```

## SQL Query

```sql
CALL pos_neg_zero(-7);
```

---

# Program 4 – Procedure to Display Weekday of a Date

## Procedure

```sql
DROP PROCEDURE IF EXISTS day_name;

DELIMITER //

CREATE PROCEDURE day_name(IN d DATE)
BEGIN

    DECLARE dat VARCHAR(20);

    SET dat = DAYNAME(d);

    SELECT d AS Date,
    dat AS WeekDay;

END //

DELIMITER ;
```

## SQL Query

```sql
CALL day_name('2024-03-16');
```

---

# Program 5 – Procedure to Find Factorial of a Number

## Procedure

```sql
DROP PROCEDURE IF EXISTS fact;

DELIMITER //

CREATE PROCEDURE fact(IN num INT)
BEGIN

    DECLARE f BIGINT DEFAULT 1;

    DECLARE n1 INT;

    SET n1 = num;

    WHILE num > 0 DO

        SET f = f * num;

        SET num = num - 1;

    END WHILE;

    SELECT n1 AS Number,
    f AS Factorial;

END //

DELIMITER ;
```

## SQL Query

```sql
CALL fact(7);
```

---

# Additional Important PL/SQL Programs

---

## 6. Prime Number Check

Checks whether a number is prime or not.

---

## 7. Greatest of Three Numbers

Finds the largest among three numbers.

---

## 8. Palindrome Number

Checks whether a number reads same forward and backward.

---

## 9. Sum of Digits

Calculates sum of digits of a number.

---

## 10. Reverse Number

Reverses digits of a number.

---

## 11. Fibonacci Series

Generates Fibonacci sequence using loops.

---

## 12. Armstrong Number

Checks whether number is an Armstrong number.

---

## 13. Multiplication Table

Displays multiplication table for a number.

---

## 14. Vowel Count

Counts vowels in a string.

---

## 15. Swap Two Numbers

Swaps two numbers using temporary variable.

---

# Advantages of Stored Procedures

- Faster execution
- Code reusability
- Better security
- Reduced redundancy
- Easy maintenance
- Modular programming

---

# Applications

- Banking systems
- Payroll systems
- ERP systems
- Hospital management systems
- Student management systems
- Inventory management systems

---

# Output

- Procedures created successfully.
- Procedures executed successfully using CALL statement.
- Conditional statements and loops executed correctly.
- Expected outputs generated.

---

# Conclusion

Successfully implemented PL/SQL concepts in MySQL using Stored Procedures, variables, conditions, loops, and procedural programming techniques.

---

# Viva Questions

1. What is PL/SQL?
2. Difference between SQL and PL/SQL.
3. What is a Stored Procedure?
4. What is DELIMITER?
5. Difference between Procedure and Function.
6. Explain IF ELSE statement.
7. Explain WHILE loop.
8. What is modular programming?
9. What is a Trigger?
10. What is a Cursor?
11. What is CALL statement?
12. Explain variable declaration.
13. Advantages of Stored Procedures.
14. Why DELIMITER is used?
15. Explain procedural programming.
16. What is a loop?
17. Explain SET statement.
18. What is the use of DECLARE?
19. Difference between IN and OUT parameters.
20. Applications of PL/SQL.