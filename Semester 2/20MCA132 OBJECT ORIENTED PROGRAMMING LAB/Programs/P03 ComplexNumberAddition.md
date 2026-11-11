# Program 3 - Add 2 Complex Numbers

## Question

Read 2 complex numbers and perform addition on the 2 complex numbers.

---

# Filename

```text
P3_ComplexNumberAddition.java
```

---

# Source Code

```java
// Program 3: Read 2 complex numbers and perform addition on the 2 complex numbers.

import java.util.Scanner;

class Complex
{
    int real, imaginary;

    Scanner sc = new Scanner(System.in);

    void input(int n)
    {
        System.out.print("\nEnter real part of the number " + n + ": ");
        real = sc.nextInt();

        System.out.print("Enter imaginary part of the number " + n + ": ");
        imaginary = sc.nextInt();
    }

    void add(Complex b)
    {
        Complex c = new Complex();

        c.real = real + b.real;
        c.imaginary = imaginary + b.imaginary;

        System.out.println("\n(" + real + " + i" + imaginary + ") + (" 
                           + b.real + " + i" + b.imaginary + ") = "
                           + c.real + " + i" + c.imaginary);
    }
}

public class P3_ComplexNumberAddition
{
    public static void main(String[] args)
    {
        Complex a = new Complex();
        Complex b = new Complex();

        a.input(1);
        b.input(2);

        a.add(b);
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
- Scanner Class
- Complex Numbers
- Encapsulation

---

# Theory

A complex number is represented in the form:

:contentReference[oaicite:0]{index=0}

Where:
- `a` → real part
- `b` → imaginary part
- `i` → imaginary unit

Addition of two complex numbers is performed by:
- adding real parts separately
- adding imaginary parts separately

Example:

:contentReference[oaicite:1]{index=1}

---

# Detailed Explanation

## Complex Class

The `Complex` class stores:
- real part
- imaginary part

Each object represents one complex number.

---

# Instance Variables

```java
int real, imaginary;
```

| Variable | Description |
|---|---|
| `real` | Stores real part |
| `imaginary` | Stores imaginary part |

---

# input() Method

```java
void input(int n)
```

This method:
- reads real part
- reads imaginary part
- stores values inside object variables

Parameter:
```text
n
```

represents complex number number.

Example:
```text
Enter real part of the number 1
```

---

# add() Method

```java
void add(Complex b)
```

This method:
- adds two complex numbers
- stores result in third object

Parameter:
```text
b
```

represents second complex number.

---

# Result Object

```java
Complex c = new Complex();
```

Used to store:
- resultant real part
- resultant imaginary part

---

# Addition Logic

## Real Part Addition

```java
c.real = real + b.real;
```

Equivalent to:

:contentReference[oaicite:2]{index=2}

---

## Imaginary Part Addition

```java
c.imaginary = imaginary + b.imaginary;
```

Equivalent to:

:contentReference[oaicite:3]{index=3}

---

# Detailed Algorithm

1. Create class named `Complex`.

2. Declare variables:
   - `real`
   - `imaginary`

3. Declare method:
```java
input(int n)
```

4. Read:
   - real part
   - imaginary part

5. Store values in object variables.

6. Declare method:
```java
add(Complex b)
```

7. Create new object:
```java
Complex c
```

8. Add:
   - real parts
   - imaginary parts

9. Store result in object `c`.

10. Display resultant complex number.

11. Create two objects:
   - `a`
   - `b`

12. Read both complex numbers.

13. Call:
```java
a.add(b);
```

14. Display result.

15. Stop program.

---

# Flow of Execution

```text
Start Program
      ↓
Create Complex Object a
      ↓
Create Complex Object b
      ↓
Read First Complex Number
      ↓
Read Second Complex Number
      ↓
Add Real Parts
      ↓
Add Imaginary Parts
      ↓
Display Result
      ↓
Stop Program
```

---

# Dry Run

Suppose:

## First Complex Number

:contentReference[oaicite:4]{index=4}

## Second Complex Number

:contentReference[oaicite:5]{index=5}

---

# Real Part Addition

:contentReference[oaicite:6]{index=6}

---

# Imaginary Part Addition

:contentReference[oaicite:7]{index=7}

---

# Result

:contentReference[oaicite:8]{index=8}

---

# Sample Input

```text
Enter real part of the number 1: 2
Enter imaginary part of the number 1: 3

Enter real part of the number 2: 4
Enter imaginary part of the number 2: 5
```

---

# Sample Output

```text
(2 + i3) + (4 + i5) = 6 + i8
```

---

# Edge Cases

## Case 1: Negative Numbers

Input:

:contentReference[oaicite:9]{index=9}

Output:

:contentReference[oaicite:10]{index=10}

---

## Case 2: Zero Values

Input:

:contentReference[oaicite:11]{index=11}

Program still works correctly.

---

# Internal Working

When:
```java
a.add(b);
```

is called:

| Variable | Represents |
|---|---|
| `real` | `a.real` |
| `imaginary` | `a.imaginary` |
| `b.real` | real part of object `b` |
| `b.imaginary` | imaginary part of object `b` |

The program:
- adds real parts
- adds imaginary parts
- stores result in object `c`

---

# Limitations

Current program:
- handles only integer values
- performs only addition
- does not simplify output format

---

# Possible Improvements

- Support floating point numbers
- Add subtraction
- Add multiplication
- Add division
- Create display method

---

# Time Complexity

:contentReference[oaicite:12]{index=12}

because only constant operations are performed.

---

# Space Complexity

:contentReference[oaicite:13]{index=13}

because only fixed variables are used.

---

# Possible Errors

## 1. InputMismatchException

Occurs when non-integer value is entered.

Example:
```text
a
```

instead of integer.

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
P3_ComplexNumberAddition.java
```

because public class name is:

```java
public class P3_ComplexNumberAddition
```

---

# Viva Questions

## Q1. What is a complex number?

:contentReference[oaicite:14]{index=14}

where:
- `a` is real part
- `b` is imaginary part

---

## Q2. How are complex numbers added?
By adding:
- real parts separately
- imaginary parts separately

---

## Q3. What is object passing?
Passing object as argument to method.

---

## Q4. Why create object `c`?
To store resultant complex number.

---

## Q5. What is encapsulation?
Combining variables and methods inside class.

---

## Q6. Why use Scanner class?
To take user input.

---

## Q7. What is the purpose of `main()` method?
Program execution starts from `main()`.

---

## Q8. What is the time complexity?

:contentReference[oaicite:15]{index=15}