# Exercise 05 – Stored Procedure

## Aim

To create a database and implement Stored Procedures in MySQL to insert records into a table under specified conditions.

---

# Theory

A Stored Procedure is a precompiled collection of SQL statements stored inside the database.

Stored procedures are used to:
- simplify database operations,
- reduce code repetition,
- improve performance,
- provide modular programming,
- and increase security.

MySQL Stored Procedures support:
- variables,
- conditions,
- loops,
- parameters,
- and procedural programming concepts.

---

# Features of Stored Procedure

- Reusable code
- Faster execution
- Reduced network traffic
- Better security
- Modular programming
- Easy maintenance

---

# Components Used

| Component | Description |
|---|---|
| CREATE PROCEDURE | Creates procedure |
| IN Parameter | Input parameter |
| DECLARE | Declares variable |
| IF ELSE | Conditional statement |
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

# SQL Query to Create Database

```sql
CREATE DATABASE STORE;

USE STORE;
```

---

# SQL Query to Create Table

```sql
CREATE TABLE Product
(
    PdtId VARCHAR(4) PRIMARY KEY,
    PName VARCHAR(20),
    Price DOUBLE(5,2),
    Quantity INT(3)
);
```

---

# Description of Table

| Column | Description |
|---|---|
| PdtId | Product ID |
| PName | Product Name |
| Price | Product Price |
| Quantity | Quantity in Stock |

---

# Stored Procedure

## Purpose

The procedure inserts product details into the Product table only when:
- price is greater than 0
- quantity is greater than or equal to 0

If conditions are not satisfied:
- record is not inserted
- no error is generated

---

# Procedure : Insertproduct

```sql
DROP PROCEDURE IF EXISTS Insertproduct;

DELIMITER //

CREATE PROCEDURE Insertproduct
(
    IN barcode INT,
    IN name VARCHAR(20),
    IN price DOUBLE(5,2),
    IN quantity INT
)

BEGIN

    DECLARE Result VARCHAR(30);

    IF price > 0 AND quantity >= 0 THEN

        INSERT INTO Product
        VALUES(barcode,name,price,quantity);

        SET Result = 'Row Inserted';

    ELSE

        SET Result = 'Row Not Inserted';

    END IF;

    SELECT Result AS Message;

END //

DELIMITER ;
```

---

# Valid Procedure Calls

```sql
CALL Insertproduct(1001,'Pen',10.50,10);

CALL Insertproduct(1002,'Pencil',5.75,15);

CALL Insertproduct(1003,'Book',25.00,5);
```

---

# Display Table

```sql
SELECT *
FROM Product;
```

---

# Invalid Procedure Calls

```sql
CALL Insertproduct(1004,'Eraser',-2,20);

CALL Insertproduct(1005,'Paper',1.25,-10);

CALL Insertproduct(1006,'Sharpner',-2.50,-20);
```

---

# Output

- Valid records inserted successfully.
- Invalid records rejected successfully.
- Procedure executed correctly.
- Product table displayed expected records.

---

# Working of Procedure

1. Procedure receives input parameters.
2. IF condition checks:
   - price > 0
   - quantity >= 0
3. If condition is true:
   - row inserted into Product table.
4. Otherwise:
   - insertion rejected.
5. Result message displayed.

---

# Advantages of Stored Procedure

- Faster execution
- Reusable code
- Better security
- Reduced redundancy
- Easy maintenance
- Modular programming

---

# Applications

- Inventory management systems
- Billing systems
- Banking applications
- ERP systems
- Product management systems
- Sales management systems

---

# Additional Important Stored Procedure Programs

1. Employee Salary Validation
2. Student Mark Calculation
3. Even/Odd Check
4. Prime Number Check
5. Factorial Program
6. Fibonacci Series
7. Armstrong Number
8. Palindrome Number
9. Greatest of Three Numbers
10. Employee Record Management

---

# Conclusion

Successfully created a database, table, and Stored Procedure in MySQL to insert product details under specified conditions.

---

# Viva Questions

1. What is a Stored Procedure?
2. Advantages of Stored Procedures.
3. What is DELIMITER?
4. Difference between SQL and PL/SQL.
5. What is an IN parameter?
6. Explain IF ELSE statement.
7. Why validation is required?
8. What is modular programming?
9. What is CALL statement?
10. Difference between Procedure and Function.
11. Why Stored Procedures are faster?
12. What is procedural programming?
13. Explain DECLARE statement.
14. Explain SET statement.
15. Applications of Stored Procedures.