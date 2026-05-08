# Program 10 - Function Overloading

## Question

Program to calculate area of different shapes using overloaded functions.

Shapes:
- Circle
- Square
- Rectangle
- Triangle

---

# Filename

```text
P10_FunctionOverloading.java
```

---

# Source Code

```java
// Program 10: Calculate area of different shapes using function overloading.

import java.util.Scanner;

class ShapeArea
{
    void area(double r)
    {
        System.out.println("Area of circle: " + String.format("%.2f", 3.14 * r * r));
    }

    void area(float r)
    {
        System.out.println("Area of square: " + (r * r));
    }

    void area(double l, double b)
    {
        System.out.println("Area of rectangle: " + (l * b));
    }

    void area(float b, float h)
    {
        System.out.println("Area of triangle: " + (0.5 * b * h));
    }
}

public class P10_FunctionOverloading
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        ShapeArea s = new ShapeArea();

        System.out.print("Enter radius of circle: ");
        s.area(sc.nextDouble());

        System.out.print("Enter length of side of square: ");
        s.area(sc.nextFloat());

        System.out.print("Enter length and breadth of rectangle: ");
        double l = sc.nextDouble();
        double b = sc.nextDouble();

        s.area(l, b);

        System.out.print("Enter breadth and height of triangle: ");
        float b1 = sc.nextFloat();
        float h = sc.nextFloat();

        s.area(b1, h);
    }
}
```

---

# Concepts Used

- Function Overloading
- Method Overloading
- Class
- Object
- Scanner Class
- Different Datatypes
- Mathematical Calculations

---

# Theory

Function overloading means:
```text
multiple methods with same name
but different parameter list
```

Java identifies overloaded methods based on:
- number of parameters
- datatype of parameters
- order of parameters

This program demonstrates:
```text
compile-time polymorphism
```

---

# Shapes and Formulas Used

| Shape | Formula |
|---|---|
| Circle | π × r² |
| Square | side × side |
| Rectangle | length × breadth |
| Triangle | 0.5 × base × height |

---

# Function Overloading

All methods have same name:
```java
area()
```

but different parameters.

---

# Overloaded Methods

## Circle

```java
void area(double r)
```

Calculates area of circle.

Formula:


::contentReference[oaicite:0]{index=0}


---

# Square

```java
void area(float r)
```

Calculates area of square.

Formula:

:contentReference[oaicite:1]{index=1}

---

# Rectangle

```java
void area(double l, double b)
```

Calculates area of rectangle.

Formula:

:contentReference[oaicite:2]{index=2}

---

# Triangle

```java
void area(float b, float h)
```

Calculates area of triangle.

Formula:


::contentReference[oaicite:3]{index=3}


---

# Detailed Explanation

## ShapeArea Class

Contains overloaded methods named:
```java
area()
```

Each method calculates:
```text
different shape area
```

---

# Method Selection

Java compiler automatically selects correct method based on:
```text
datatype and number of arguments
```

Example:

```java
s.area(5.0);
```

calls:
```java
area(double r)
```

---

# String.format()

```java
String.format("%.2f", value)
```

Formats decimal output to:
```text
2 decimal places
```

---

# Scanner Class

Used to read:
- double values
- float values

from user.

---

# Detailed Algorithm

1. Create class:
```java
ShapeArea
```

2. Create overloaded methods:
```java
area()
```

3. Define:
```java
area(double r)
```

for circle.

4. Define:
```java
area(float r)
```

for square.

5. Define:
```java
area(double l, double b)
```

for rectangle.

6. Define:
```java
area(float b, float h)
```

for triangle.

7. Create main method.

8. Create object:
```java
ShapeArea s
```

9. Read radius of circle.

10. Call:
```java
area(double r)
```

11. Read side of square.

12. Call:
```java
area(float r)
```

13. Read rectangle dimensions.

14. Call:
```java
area(double l, double b)
```

15. Read triangle dimensions.

16. Call:
```java
area(float b, float h)
```

17. Display areas.

18. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create Object
   ↓
Read Circle Radius
   ↓
Calculate Circle Area
   ↓
Read Square Side
   ↓
Calculate Square Area
   ↓
Read Rectangle Dimensions
   ↓
Calculate Rectangle Area
   ↓
Read Triangle Dimensions
   ↓
Calculate Triangle Area
   ↓
Display Results
   ↓
Stop
```

---

# Sample Input

```text
Enter radius of circle: 5

Enter length of side of square: 4

Enter length and breadth of rectangle: 5 6

Enter breadth and height of triangle: 4 3
```

---

# Sample Output

```text
Area of circle: 78.50

Area of square: 16.0

Area of rectangle: 30.0

Area of triangle: 6.0
```

---

# Dry Run

Circle radius:
```text
5
```

Calculation:

:contentReference[oaicite:4]{index=4}

---

Rectangle:
```text
5 × 6
```

Calculation:

:contentReference[oaicite:5]{index=5}

---

# Internal Working

Compiler checks:
- method name
- parameter datatype
- parameter count

to select correct overloaded method.

This is:
```text
compile-time polymorphism
```

---

# Advantages of Function Overloading

- Improves readability
- Reduces method name complexity
- Increases code reusability
- Supports polymorphism

---

# Time Complexity

Each calculation:

:contentReference[oaicite:6]{index=6}

because only direct mathematical operations are performed.

---

# Space Complexity

:contentReference[oaicite:7]{index=7}

---

# Edge Cases

## Case 1: Radius = 0

Circle area:

:contentReference[oaicite:8]{index=8}

---

## Case 2: Negative Values

Program still calculates mathematically,
but dimensions should ideally be positive.

---

## Case 3: Decimal Inputs

Program supports decimal values using:
- float
- double

---

# Possible Improvements

- Add validation for negative inputs
- Add menu-driven approach
- Use Math.PI instead of 3.14

---

# Possible Errors

## 1. InputMismatchException

Occurs when invalid datatype entered.

Example:
```text
abc
```

instead of numeric value.

---

## 2. Precision Issues

Float values may lose precision.

---

# Viva Questions

## Q1. What is function overloading?
Using same method name with different parameters.

---

## Q2. What is polymorphism?
Ability of method to behave differently.

---

## Q3. Which polymorphism is used here?
Compile-time polymorphism.

---

## Q4. Can methods differ only by return type?
No.

---

## Q5. What is method signature?
Method name + parameter list.

---

## Q6. Difference between float and double?

| float | double |
|---|---|
| 4 bytes | 8 bytes |
| Less precision | More precision |

---

## Q7. Why use overloaded methods?
To perform related operations using same method name.

---

## Q8. What is String.format() used for?
Formatting output.

---

## Q9. Which method calculates circle area?

```java
area(double r)
```

---

## Q10. What is time complexity?

:contentReference[oaicite:9]{index=9}