-- EXERCISE 5 : STORED PROCEDURE

-- CREATE DATABASE

CREATE DATABASE STORE;

USE STORE;

SHOW DATABASES;

SELECT DATABASE();

-- CREATE TABLE : PRODUCT

CREATE TABLE Product
(
    PdtId VARCHAR(4) PRIMARY KEY,
    PName VARCHAR(20),
    Price DOUBLE(5,2),
    Quantity INT(3)
);

-- DISPLAY TABLE

DESC Product;

-- DROP PROCEDURE IF EXISTS

DROP PROCEDURE IF EXISTS Insertproduct;

-- CREATE PROCEDURE

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

-- INSERT VALID VALUES

CALL Insertproduct(1001,'Pen',10.50,10);

CALL Insertproduct(1002,'Pencil',5.75,15);

CALL Insertproduct(1003,'Book',25.00,5);

-- DISPLAY TABLE

SELECT *
FROM Product;

-- INSERT INVALID VALUES

CALL Insertproduct(1004,'Eraser',-2,20);

CALL Insertproduct(1005,'Paper',1.25,-10);

CALL Insertproduct(1006,'Sharpner',-2.50,-20);

-- DISPLAY TABLE

SELECT *
FROM Product;