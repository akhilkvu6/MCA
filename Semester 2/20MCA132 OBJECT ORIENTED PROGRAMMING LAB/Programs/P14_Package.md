# Program 14 - Package

## Question

Create a Graphics package that has classes and interfaces for figures:
- Rectangle
- Triangle
- Square
- Circle

Test the package by finding the area of these figures.

---

# Filename Structure

```text
Programs/
│
├── Graphics/
│   ├── Figure.java
│   ├── Circle.java
│   ├── Rectangle.java
│   ├── Square.java
│   └── Triangle.java
│
└── P14_Package.java
```

---

# What is a Package in Java?

A package in Java is:
```text
a collection of related classes and interfaces
```

Packages are used to:
- organize code
- avoid naming conflicts
- improve modularity
- improve reusability

---

# Graphics Package

In this program:

```java
package Graphics;
```

creates a package named:
```text
Graphics
```

All shape classes are stored inside this package.

---

# Advantages of Packages

- Better organization
- Code reusability
- Avoids class name conflicts
- Easier maintenance
- Access protection

---

# Interface Used

```java
interface Figure
```

contains:
```java
area()
```

method.

All shape classes implement:
```text
Figure interface
```

---

# Package Structure Explanation

## Figure.java

Contains:
```java
interface Figure
```

Defines common method:
```java
area()
```

---

# Circle.java

Implements:
```java
Figure
```

Calculates:
```text
Area of Circle
```

Formula:


::contentReference[oaicite:0]{index=0}


---

# Rectangle.java

Calculates:
```text
Area of Rectangle
```

Formula:

:contentReference[oaicite:1]{index=1}

---

# Square.java

Calculates:
```text
Area of Square
```

Formula:

:contentReference[oaicite:2]{index=2}

---

# Triangle.java

Calculates:
```text
Area of Triangle
```

Formula:


::contentReference[oaicite:3]{index=3}


---

# Main Program

```java
P14_Package.java
```

imports:
```java
import Graphics.*;
```

This imports all classes from:
```text
Graphics package
```

---

# Source Code

# Figure.java

```java
package Graphics;

interface Figure
{
    public void area();
}
```

---

# Circle.java

```java
package Graphics;

public class Circle implements Figure
{
    double radius;

    public Circle(double r)
    {
        radius = r;
    }

    public void area()
    {
        System.out.println("Area of circle: " +
        String.format("%.2f",(3.14 * radius * radius)));
    }
}
```

---

# Rectangle.java

```java
package Graphics;

public class Rectangle implements Figure
{
    double length;
    double breadth;

    public Rectangle(double l,double b)
    {
        length = l;
        breadth = b;
    }

    public void area()
    {
        System.out.println("Area of Rectangle: " +
        String.format("%.2f",(length * breadth)));
    }
}
```

---

# Square.java

```java
package Graphics;

public class Square implements Figure
{
    double length;

    public Square(double l)
    {
        length = l;
    }

    public void area()
    {
        System.out.println("Area of Square: " +
        String.format("%.2f",(length * length)));
    }
}
```

---

# Triangle.java

```java
package Graphics;

public class Triangle implements Figure
{
    double breadth;
    double height;

    public Triangle(double b,double h)
    {
        breadth = b;
        height = h;
    }

    public void area()
    {
        System.out.println("Area of Triangle: " +
        String.format("%.2f",(0.5 * breadth * height)));
    }
}
```

---

# P14_Package.java

```java
import java.util.Scanner;
import Graphics.*;

public class P14_Package
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("\nEnter radius of circle: ");

        double cr = sc.nextDouble();

        Graphics.Circle c = new Graphics.Circle(cr);

        c.area();

        System.out.print("\nEnter length and breadth of rectangle: ");

        double l = sc.nextDouble();
        double b = sc.nextDouble();

        Graphics.Rectangle r = new Graphics.Rectangle(l,b);

        r.area();

        System.out.print("\nEnter side of square: ");

        l = sc.nextDouble();

        Graphics.Square s = new Graphics.Square(l);

        s.area();

        System.out.print("\nEnter height and breadth of triangle: ");

        l = sc.nextDouble();
        b = sc.nextDouble();

        Graphics.Triangle t = new Graphics.Triangle(b,l);

        t.area();
    }
}
```

---

# Detailed Algorithm

1. Create package:
```java
Graphics
```

2. Create interface:
```java
Figure
```

3. Declare:
```java
area()
```

method.

4. Create classes:
- Circle
- Rectangle
- Square
- Triangle

5. Implement:
```java
Figure
```

6. Define:
```java
area()
```

method in each class.

7. Create:
```java
P14_Package.java
```

8. Import package:
```java
import Graphics.*;
```

9. Read dimensions from user.

10. Create objects of shapes.

11. Call:
```java
area()
```

methods.

12. Display areas.

13. Stop program.

---

# How Package Works

When compiler sees:

```java
package Graphics;
```

Java places compiled class inside:
```text
Graphics folder
```

Main program imports classes using:
```java
import Graphics.*;
```

This allows:
```text
using package classes in another file
```

---

# How to Compile

Open terminal inside:
```text
Programs folder
```

---

# Step 1: Compile Package Classes

```bash
javac Graphics/*.java
```

---

# Step 2: Compile Main Program

```bash
javac P14_Package.java
```

---

# Step 3: Run Program

```bash
java P14_Package
```

---

# Alternative Compilation

Compile everything together:

```bash
javac Graphics/*.java P14_Package.java
```

Run:

```bash
java P14_Package
```

---

# Flow of Execution

```text
Start
   ↓
Import Graphics Package
   ↓
Read Circle Radius
   ↓
Calculate Circle Area
   ↓
Read Rectangle Dimensions
   ↓
Calculate Rectangle Area
   ↓
Read Square Side
   ↓
Calculate Square Area
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

Enter length and breadth of rectangle: 4 6

Enter side of square: 4

Enter height and breadth of triangle: 5 4
```

---

# Sample Output

```text
Area of circle: 78.50

Area of Rectangle: 24.00

Area of Square: 16.00

Area of Triangle: 10.00
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
4 × 6
```

Calculation:

:contentReference[oaicite:5]{index=5}

---

# Internal Working

Package organizes:
```text
multiple related classes
```

Each class independently calculates:
```text
shape area
```

Main program accesses package classes using:
```java
import
```

statement.

---

# Time Complexity

Each area calculation:

:contentReference[oaicite:6]{index=6}

---

# Space Complexity

:contentReference[oaicite:7]{index=7}

---

# Advantages

- Modular programming
- Better code organization
- Reusable classes
- Improved maintainability

---

# Limitations

- More files to manage
- Compilation slightly complex for beginners

---

# Edge Cases

## Case 1: Radius = 0

Area:

:contentReference[oaicite:8]{index=8}

---

## Case 2: Negative Dimensions

Program still calculates mathematically.

---

## Case 3: Missing Package Folder

Compilation error occurs.

---

# Possible Errors

## 1. Package Not Found

Occurs if:
```text
Graphics folder missing
```

---

## 2. Class Not Found Exception

Occurs if classes not compiled.

---

## 3. InputMismatchException

Occurs for invalid input datatype.

---

# Viva Questions

## Q1. What is a package in Java?
Collection of related classes and interfaces.

---

## Q2. Which keyword is used to create package?

```java
package
```

---

## Q3. Which keyword is used to import package?

```java
import
```

---

## Q4. What is interface?
Blueprint containing abstract methods.

---

## Q5. What is abstraction?
Hiding implementation details.

---

## Q6. Why use packages?
Code organization and reusability.

---

## Q7. Can package contain interfaces?
Yes.

---

## Q8. What is the folder name here?
Graphics.

---

## Q9. Which method is common to all classes?

```java
area()
```

---

## Q10. What is time complexity?

:contentReference[oaicite:9]{index=9}