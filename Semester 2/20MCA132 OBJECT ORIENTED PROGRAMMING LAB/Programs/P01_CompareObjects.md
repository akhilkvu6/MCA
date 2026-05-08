# Program 1 - Lowest Product Price

## Question

Define a class `Product` with data members `pcode`, `pname`, `price`.  
Create 3 objects of the class and find the product having the lowest price.

---

# Filename

```text
P1_CompareObjects.java
```

---

# Source Code

```java
// Program 1: Define a class Product with data members pcode, pname, price. Create 3 objects of the class and find the product having the lowest price.

import java.util.Scanner;

class Product
{
    String pcode, pname;
    int price;

    void details(int n)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("\nEnter product code for item " + n + ": ");
        pcode = sc.next();

        System.out.print("Enter product name for item " + n + ": ");
        pname = sc.next();

        System.out.print("Enter product price for item " + n + ": ");
        price = sc.nextInt();
    }

    void lowest(Product a, Product b)
    {
        if(price < a.price && price < b.price)
        {
            System.out.println("\nProduct " + pname + " has lowest price");
        }
        else if(a.price < b.price)
        {
            System.out.println("\nProduct " + a.pname + " has lowest price");
        }
        else
        {
            System.out.println("\nProduct " + b.pname + " has lowest price");
        }
    }
}

public class P1_CompareObjects
{
    public static void main(String[] args)
    {
        Product p1 = new Product();
        Product p2 = new Product();
        Product p3 = new Product();

        p1.details(1);
        p2.details(2);
        p3.details(3);

        p1.lowest(p2, p3);
    }
}
```

---

# Concepts Used

- Class
- Object
- Instance Variables
- Methods
- Object Passing
- Conditional Statements
- Scanner Class
- Encapsulation

---

# Detailed Explanation

## Product Class

The `Product` class stores product details:
- product code
- product name
- product price

Each object created from the class stores separate values.

---

## Instance Variables

```java
String pcode, pname;
int price;
```

| Variable | Description |
|---|---|
| `pcode` | Stores product code |
| `pname` | Stores product name |
| `price` | Stores product price |

---

## details() Method

```java
void details(int n)
```

This method is used to:
- read product details from the user
- store values inside object variables

Parameter:
```text
n
```

represents product number.

Example:
```text
Enter product code for item 1
```

---

## Scanner Object

```java
Scanner sc = new Scanner(System.in);
```

Used for taking keyboard input.

---

## lowest() Method

```java
void lowest(Product a, Product b)
```

This method compares prices of:
- current object
- object `a`
- object `b`

Method call:
```java
p1.lowest(p2, p3);
```

means:
```text
Compare:
p1.price
p2.price
p3.price
```

---

# Logic Used

## First Condition

```java
if(price < a.price && price < b.price)
```

Checks whether current object's price is smallest.

Equivalent meaning:
```text
p1.price < p2.price AND p1.price < p3.price
```

---

## Second Condition

```java
else if(a.price < b.price)
```

If first condition fails:
- compare `p2` and `p3`

---

## Else Block

```java
else
```

If both previous conditions fail:
- third product has lowest price.

---

# Detailed Algorithm

1. Create a class named `Product`. Declare instance variables:
   - `pcode`
   - `pname`
   - `price`

2. Declare a method:
```java
details(int n)
```

- Prompt the user to enter product details for the `n`th item.
- Read the product code, product name, and product price from the user.
- Store the values in the corresponding instance variables.

3. Declare a method:
```java
lowest(Product a, Product b)
```

- Compare the price of:
  - current object (`this.price`)
  - object `a`
  - object `b`

- If:
```java
this.price < a.price && this.price < b.price
```
then current object's product has the lowest price.

- Else if:
```java
a.price < b.price
```
then object `a` has the lowest price.

- Otherwise object `b` has the lowest price.

- Display the product having the lowest price.

4. Create three objects of `Product` class:
   - `p1`
   - `p2`
   - `p3`

5. Call the `details()` method for each object.

6. Call:
```java
p1.lowest(p2, p3);
```

to compare all three products.

7. Display the product having minimum price.

8. Stop the program.

---

# Dry Run

Suppose:

| Product | Price |
|---|---|
| p1 | 500 |
| p2 | 300 |
| p3 | 700 |

---

## Step 1

Check:
```java
price < a.price && price < b.price
```

becomes:
```text
500 < 300 && 500 < 700
```

Result:
```text
false
```

---

## Step 2

Check:
```java
a.price < b.price
```

becomes:
```text
300 < 700
```

Result:
```text
true
```

---

## Output

```text
Product p2 has lowest price
```

---

# Sample Input

```text
Enter product code for item 1: P101
Enter product name for item 1: Pen
Enter product price for item 1: 50

Enter product code for item 2: P102
Enter product name for item 2: Book
Enter product price for item 2: 30

Enter product code for item 3: P103
Enter product name for item 3: Bag
Enter product price for item 3: 70
```

---

# Sample Output

```text
Product Book has lowest price
```

---

# Edge Cases

## Case 1: Equal Prices

Input:
```text
500
500
700
```

Current logic may not correctly identify duplicate minimum values.

---

## Case 2: All Prices Same

Input:
```text
500
500
500
```

Control goes to `else` block.

---

# Limitations

Current logic does not properly handle:
- equal prices
- duplicate minimum values

Better condition:
```java
if(price <= a.price && price <= b.price)
```

---

# Possible Errors

## 1. InputMismatchException

Occurs when:
```text
abc
```

is entered instead of integer value.

---

## 2. Missing Import Statement

If:
```java
import java.util.Scanner;
```

is removed.

Error:
```text
Scanner cannot be resolved to a type
```

---

## 3. File Name Mismatch

Filename must be:

```text
P1_CompareObjects.java
```

because public class name is:

```java
public class P1_CompareObjects
```

---

# Time Complexity

```text
O(1)
```

Reason:
- fixed number of comparisons
- no loops used

---

# Viva Questions

## Q1. What is a class?
A class is a blueprint for creating objects.

## Q2. What is an object?
Object is an instance of a class.

## Q3. What are instance variables?
Variables declared inside class but outside methods.

## Q4. What is encapsulation?
Combining data and methods inside one class.

## Q5. Why use Scanner class?
To read user input.

## Q6. What is object passing?
Passing complete objects as method arguments.

## Q7. What is the use of `new` keyword?
Allocates memory for object creation.

## Q8. What is method calling?
Invoking a method using an object.

## Q9. What is the purpose of `main()` method?
Program execution starts from `main()`.

## Q10. What is time complexity of this program?
```text
O(1)
```
because only constant comparisons are performed.