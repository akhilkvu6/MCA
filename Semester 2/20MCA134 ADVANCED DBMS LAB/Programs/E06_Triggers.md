# Exercise 06 – Triggers

## Aim

To create tables and implement Triggers in MySQL to automatically update available stock quantity after each product sale.

---

# Theory

A Trigger is a database object that automatically executes when an INSERT, UPDATE, or DELETE operation occurs on a table.

Triggers are used to:
- maintain data consistency,
- automate database operations,
- validate data,
- and maintain audit/history records.

In this exercise, a trigger automatically updates product stock quantity whenever a product is sold.

---

# Features of Triggers

- Automatic execution
- Maintains data integrity
- Reduces manual work
- Supports event-driven programming
- Improves consistency

---

# Types of Triggers

| Trigger Type | Executes |
|---|---|
| BEFORE INSERT | Before inserting row |
| AFTER INSERT | After inserting row |
| BEFORE UPDATE | Before updating row |
| AFTER UPDATE | After updating row |
| BEFORE DELETE | Before deleting row |
| AFTER DELETE | After deleting row |

---

# Components Used

| Component | Description |
|---|---|
| CREATE TRIGGER | Creates trigger |
| AFTER INSERT | Executes after insertion |
| FOR EACH ROW | Executes for every inserted row |
| NEW | Refers to newly inserted row |
| UPDATE | Updates table values |
| DELIMITER | Changes statement terminator |

---

# DELIMITER

## Purpose

MySQL uses semicolon `;` as default statement terminator.

For triggers, delimiter is temporarily changed using:

```sql
DELIMITER //
```

After trigger creation:

```sql
DELIMITER ;
```

restores the default delimiter.

---

# General Syntax of Trigger

```sql
DELIMITER //

CREATE TRIGGER trigger_name

AFTER INSERT
ON table_name

FOR EACH ROW

BEGIN

    -- SQL statements

END //

DELIMITER ;
```

---

# Database Creation

```sql
CREATE DATABASE stores;

USE stores;
```

---

# Table Creation

---

# Table : Product

```sql
CREATE TABLE Product
(
    PdtId INT PRIMARY KEY,
    Pname VARCHAR(20),
    Price DOUBLE(5,2),
    Qtyinstock INT
);
```

---

# Table : Sale

```sql
CREATE TABLE Sale
(
    saleId INT PRIMARY KEY,
    Deliveryaddress VARCHAR(50)
);
```

---

# Table : Saleitem

```sql
CREATE TABLE Saleitem
(
    saleId INT,
    PdtId INT,
    Qty INT,

    PRIMARY KEY(saleId,PdtId),

    FOREIGN KEY(saleId)
    REFERENCES Sale(saleId),

    FOREIGN KEY(PdtId)
    REFERENCES Product(PdtId)
);
```

---

# Description of Tables

| Table | Purpose |
|---|---|
| Product | Stores product details |
| Sale | Stores sale information |
| Saleitem | Stores sold products |

---

# Insert Values into Product Table

```sql
INSERT INTO Product
(PdtId, Pname, Price, Qtyinstock)

VALUES
(101,'Pencil',5.00,10),
(102,'Pen',3.00,10);
```

---

# Insert Values into Sale Table

```sql
INSERT INTO Sale
(saleId,Deliveryaddress)

VALUES
(001,'home123'),
(002,'home345');
```

---

# Trigger : updateAvailabeQuantity

## Purpose

The trigger automatically updates available stock quantity whenever a product is sold.

After inserting values into Saleitem table:
- sold quantity is deducted from Product table stock.

---

# Trigger Definition

```sql
DROP TRIGGER IF EXISTS updateAvailabeQuantity;

DELIMITER //

CREATE TRIGGER updateAvailabeQuantity

AFTER INSERT
ON Saleitem

FOR EACH ROW

BEGIN

    UPDATE Product

    SET Qtyinstock = Qtyinstock - NEW.Qty

    WHERE PdtId = NEW.PdtId;

END //

DELIMITER ;
```

---

# Explanation of Trigger

| Statement | Description |
|---|---|
| AFTER INSERT | Trigger executes after insertion |
| FOR EACH ROW | Executes for every inserted row |
| NEW.Qty | Quantity from newly inserted row |
| NEW.PdtId | Product ID from inserted row |

---

# Insert Values into Saleitem Table

```sql
INSERT INTO Saleitem
VALUES (001,102,8);

INSERT INTO Saleitem
VALUES (002,101,3);

INSERT INTO Saleitem
VALUES (002,102,1);
```

---

# Display Product Table

```sql
SELECT *
FROM Product;
```

---

# Display Saleitem Table

```sql
SELECT *
FROM Saleitem;
```

---

# Working of Trigger

1. Product sold details inserted into Saleitem table.
2. AFTER INSERT trigger automatically executes.
3. Trigger identifies:
   - product id,
   - sold quantity.
4. Product table stock updated automatically.
5. New available quantity displayed.

---

# OLD and NEW Keywords

| Keyword | Description |
|---|---|
| OLD | Existing row value |
| NEW | Newly inserted or updated value |

---

# Applications of Triggers

- Inventory management systems
- Banking systems
- Audit systems
- Billing systems
- ERP systems
- Automatic logging systems

---

# Advantages of Triggers

- Automatic execution
- Maintains consistency
- Reduces manual work
- Improves data integrity
- Supports automation

---

# Output

- Tables created successfully.
- Trigger created successfully.
- Product quantities updated automatically after each sale.
- Expected output generated successfully.

---

# Conclusion

Successfully created tables and implemented a Trigger in MySQL to automatically update product stock quantity after product sales.

---

# Viva Questions

1. What is a Trigger?
2. Difference between BEFORE and AFTER trigger.
3. What is FOR EACH ROW?
4. What is NEW keyword?
5. What is OLD keyword?
6. Applications of Triggers.
7. Advantages of Triggers.
8. Difference between Trigger and Procedure.
9. What is automatic execution?
10. What is data integrity?
11. Explain AFTER INSERT trigger.
12. Why DELIMITER is used?
13. What is event-driven programming?
14. Explain UPDATE statement.
15. What is stock management?