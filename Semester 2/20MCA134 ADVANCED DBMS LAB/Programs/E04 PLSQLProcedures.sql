-- EXERCISE 4 : PLSQL PROCEDURES

CREATE DATABASE plsql;

USE plsql;

SHOW DATABASES;

SELECT DATABASE();

-- 1. PROCEDURE TO CHECK EVEN OR ODD

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

-- CALL PROCEDURE

CALL even_odd(7);

-- 2. PROCEDURE TO DISPLAY GRADE FOR A MARK

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

-- CALL PROCEDURE

CALL grade(87);

-- 3. PROCEDURE TO CHECK POSITIVE, NEGATIVE OR ZERO

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

-- CALL PROCEDURE

CALL pos_neg_zero(-7);

-- 4. PROCEDURE TO DISPLAY WEEKDAY OF A DATE

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

-- CALL PROCEDURE

CALL day_name('2024-03-16');

-- 5. PROCEDURE TO FIND FACTORIAL OF A NUMBER

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

-- CALL PROCEDURE

CALL fact(7);


-- 1. PROCEDURE TO CHECK PRIME NUMBER

DROP PROCEDURE IF EXISTS prime_check;

DELIMITER //

CREATE PROCEDURE prime_check(IN num INT)
BEGIN

    DECLARE i INT DEFAULT 2;
    DECLARE flag INT DEFAULT 0;

    WHILE i <= num / 2 DO

        IF num % i = 0 THEN
            SET flag = 1;
        END IF;

        SET i = i + 1;

    END WHILE;

    IF flag = 0 THEN
        SELECT num AS Number, 'Prime' AS Result;
    ELSE
        SELECT num AS Number, 'Not Prime' AS Result;
    END IF;

END //

DELIMITER ;

CALL prime_check(7);

-- 2. PROCEDURE TO FIND GREATEST OF THREE NUMBERS

DROP PROCEDURE IF EXISTS greatest;

DELIMITER //

CREATE PROCEDURE greatest(IN a INT, IN b INT, IN c INT)
BEGIN

    DECLARE g INT;

    IF a > b AND a > c THEN
        SET g = a;

    ELSEIF b > c THEN
        SET g = b;

    ELSE
        SET g = c;

    END IF;

    SELECT g AS Greatest_Number;

END //

DELIMITER ;

CALL greatest(10,20,30);

-- 3. PROCEDURE TO CHECK PALINDROME NUMBER

DROP PROCEDURE IF EXISTS palindrome;

DELIMITER //

CREATE PROCEDURE palindrome(IN num INT)
BEGIN

    DECLARE rev INT DEFAULT 0;
    DECLARE rem INT;
    DECLARE temp INT;

    SET temp = num;

    WHILE temp > 0 DO

        SET rem = temp % 10;
        SET rev = rev * 10 + rem;
        SET temp = FLOOR(temp / 10);

    END WHILE;

    IF rev = num THEN
        SELECT num AS Number, 'Palindrome' AS Result;
    ELSE
        SELECT num AS Number, 'Not Palindrome' AS Result;
    END IF;

END //

DELIMITER ;

CALL palindrome(121);

-- 4. PROCEDURE TO FIND SUM OF DIGITS

DROP PROCEDURE IF EXISTS sum_digits;

DELIMITER //

CREATE PROCEDURE sum_digits(IN num INT)
BEGIN

    DECLARE s INT DEFAULT 0;
    DECLARE rem INT;
    DECLARE temp INT;

    SET temp = num;

    WHILE temp > 0 DO

        SET rem = temp % 10;
        SET s = s + rem;
        SET temp = FLOOR(temp / 10);

    END WHILE;

    SELECT num AS Number,
    s AS Sum_Of_Digits;

END //

DELIMITER ;

CALL sum_digits(1234);

-- 5. PROCEDURE TO REVERSE A NUMBER

DROP PROCEDURE IF EXISTS reverse_number;

DELIMITER //

CREATE PROCEDURE reverse_number(IN num INT)
BEGIN

    DECLARE rev INT DEFAULT 0;
    DECLARE rem INT;
    DECLARE temp INT;

    SET temp = num;

    WHILE temp > 0 DO

        SET rem = temp % 10;
        SET rev = rev * 10 + rem;
        SET temp = FLOOR(temp / 10);

    END WHILE;

    SELECT num AS Original_Number,
    rev AS Reversed_Number;

END //

DELIMITER ;

CALL reverse_number(12345);

-- 6. PROCEDURE TO GENERATE FIBONACCI SERIES

DROP PROCEDURE IF EXISTS fibonacci;

DELIMITER //

CREATE PROCEDURE fibonacci(IN n INT)
BEGIN

    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 1;
    DECLARE c INT;
    DECLARE i INT DEFAULT 1;

    WHILE i <= n DO

        SELECT a AS Fibonacci_Number;

        SET c = a + b;
        SET a = b;
        SET b = c;

        SET i = i + 1;

    END WHILE;

END //

DELIMITER ;

CALL fibonacci(10);

-- 7. PROCEDURE TO CHECK ARMSTRONG NUMBER

DROP PROCEDURE IF EXISTS armstrong;

DELIMITER //

CREATE PROCEDURE armstrong(IN num INT)
BEGIN

    DECLARE sum1 INT DEFAULT 0;
    DECLARE rem INT;
    DECLARE temp INT;

    SET temp = num;

    WHILE temp > 0 DO

        SET rem = temp % 10;
        SET sum1 = sum1 + (rem * rem * rem);
        SET temp = FLOOR(temp / 10);

    END WHILE;

    IF sum1 = num THEN
        SELECT num AS Number, 'Armstrong' AS Result;
    ELSE
        SELECT num AS Number, 'Not Armstrong' AS Result;
    END IF;

END //

DELIMITER ;

CALL armstrong(153);

-- 8. PROCEDURE TO DISPLAY MULTIPLICATION TABLE

DROP PROCEDURE IF EXISTS multiplication_table;

DELIMITER //

CREATE PROCEDURE multiplication_table(IN num INT)
BEGIN

    DECLARE i INT DEFAULT 1;

    WHILE i <= 10 DO

        SELECT num AS Number,
        i AS Multiplier,
        num * i AS Result;

        SET i = i + 1;

    END WHILE;

END //

DELIMITER ;

CALL multiplication_table(5);

-- 9. PROCEDURE TO COUNT VOWELS IN A STRING

DROP PROCEDURE IF EXISTS vowel_count;

DELIMITER //

CREATE PROCEDURE vowel_count(IN str VARCHAR(100))
BEGIN

    DECLARE i INT DEFAULT 1;
    DECLARE len INT;
    DECLARE ch CHAR(1);
    DECLARE count1 INT DEFAULT 0;

    SET len = LENGTH(str);

    WHILE i <= len DO

        SET ch = LOWER(SUBSTRING(str,i,1));

        IF ch IN ('a','e','i','o','u') THEN
            SET count1 = count1 + 1;
        END IF;

        SET i = i + 1;

    END WHILE;

    SELECT str AS String_Value,
    count1 AS Vowel_Count;

END //

DELIMITER ;

CALL vowel_count('Database');

-- 10. PROCEDURE TO SWAP TWO NUMBERS

DROP PROCEDURE IF EXISTS swap_numbers;

DELIMITER //

CREATE PROCEDURE swap_numbers(IN a INT, IN b INT)
BEGIN

    DECLARE temp INT;

    SET temp = a;
    SET a = b;
    SET b = temp;

    SELECT a AS First_Number,
    b AS Second_Number;

END //

DELIMITER ;

CALL swap_numbers(10,20);