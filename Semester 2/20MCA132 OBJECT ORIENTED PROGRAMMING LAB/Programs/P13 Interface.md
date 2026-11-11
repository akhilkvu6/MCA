# Program 13 - Interface

## Question

Create an interface having prototypes of functions:
- area()
- perimeter()

Create two classes:
- Circle
- Rectangle

which implement the above interface.

Create a menu driven program to find area and perimeter of objects.

---

# Filename

```text
P13_Interface.java
```

---

# Source Code

```java
// Program 13: Interface implementation using Circle and Rectangle.

import java.util.Scanner;

interface Shape
{
    public void area();
    public void perimeter();
}

class Circle implements Shape
{
    double radius;

    Circle(double r)
    {
        radius = r;
    }

    public void area()
    {
        System.out.println("Area of circle: " +
        String.format("%.2f",(3.14 * radius * radius)));
    }

    public void perimeter()
    {
        System.out.println("Perimeter of circle: " +
        String.format("%.2f",(2 * 3.14 * radius)));
    }
}

class Rectangle implements Shape
{
    double length,breadth;

    Rectangle(double l,double b)
    {
        length = l;
        breadth = b;
    }

    public void area()
    {
        System.out.println("Area of rectangle: " +
        String.format("%.2f",(length * breadth)));
    }

    public void perimeter()
    {
        System.out.println("Perimeter of rectangle: " +
        String.format("%.2f",(2 * (length + breadth))));
    }
}

public class P13_Interface
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int ch;

        do
        {
            System.out.print("------------------\n1.Circle\n2.Rectangle\n3.Exit\n------------------\nEnter your choice: ");

            ch = sc.nextInt();

            switch(ch)
            {
                case 1:

                    System.out.print("Enter radius of circle: ");

                    double r = sc.nextDouble();

                    Circle c = new Circle(r);

                    c.area();
                    c.perimeter();

                    break;

                case 2:

                    System.out.print("Enter length and breadth of rectangle: ");

                    double l = sc.nextDouble();
                    double b = sc.nextDouble();

                    Rectangle r1 = new Rectangle(l,b);

                    r1.area();
                    r1.perimeter();

                    break;

                case 3:

                    System.out.println("Exiting...");

                    break;

                default:

                    System.out.println("Invalid choice!");
            }

        } while(ch != 3);
    }
}
```

---

# Concepts Used

- Interface
- Abstraction
- Implements Keyword
- Method Overriding
- Menu Driven Program
- Switch Case
- do-while Loop
- Scanner Class
- Object Oriented Programming

---

# Theory

An interface in Java is used to achieve:
```text
abstraction
```

Interface contains:
```text
abstract methods
```

which must be implemented by classes.

---

# Interface

```java
interface Shape
```

contains:
- area()
- perimeter()

These methods do not contain method body.

---

# Abstract Methods

```java
public void area();

public void perimeter();
```

These methods:
- are abstract
- must be implemented by classes

---

# implements Keyword

```java
class Circle implements Shape
```

Used to implement interface methods.

---

# Circle Class

Implements:
- area()
- perimeter()

for circle.

---

# Rectangle Class

Implements:
- area()
- perimeter()

for rectangle.

---

# Formulas Used

## Area of Circle


::contentReference[oaicite:0]{index=0}


---

# Perimeter of Circle

:contentReference[oaicite:1]{index=1}

---

# Area of Rectangle

:contentReference[oaicite:2]{index=2}

---

# Perimeter of Rectangle

:contentReference[oaicite:3]{index=3}

---

# Menu Driven Program

Program repeatedly displays menu using:
```java
do-while
```

loop.

---

# Switch Case

Used to execute:
```text
different operations
```

based on user choice.

---

# Detailed Algorithm

1. Create interface:
```java
Shape
```

2. Declare methods:
```java
area()
```

and:
```java
perimeter()
```

3. Create class:
```java
Circle
```

4. Implement:
```java
Shape
```

5. Declare:
```java
radius
```

6. Implement:
```java
area()
```

and:
```java
perimeter()
```

7. Create class:
```java
Rectangle
```

8. Implement:
```java
Shape
```

9. Declare:
```java
length
```

and:
```java
breadth
```

10. Implement:
```java
area()
```

and:
```java
perimeter()
```

11. In main method:
   - display menu
   - read choice

12. Use switch case.

13. Create objects based on user choice.

14. Call:
```java
area()
```

and:
```java
perimeter()
```

15. Repeat until user exits.

16. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Display Menu
   ↓
Read Choice
   ↓
Create Object
   ↓
Calculate Area
   ↓
Calculate Perimeter
   ↓
Display Result
   ↓
Exit?
   ↓
Repeat / Stop
```

---

# Sample Input

```text
1
5

2
4
6

3
```

---

# Sample Output

```text
------------------
1.Circle
2.Rectangle
3.Exit
------------------
Enter your choice: 1

Enter radius of circle: 5

Area of circle: 78.50
Perimeter of circle: 31.40


------------------
1.Circle
2.Rectangle
3.Exit
------------------
Enter your choice: 2

Enter length and breadth of rectangle: 4 6

Area of rectangle: 24.00
Perimeter of rectangle: 20.00


------------------
1.Circle
2.Rectangle
3.Exit
------------------
Enter your choice: 3

Exiting...
```

---

# Dry Run

Radius:
```text
5
```

Area calculation:

:contentReference[oaicite:4]{index=4}

Perimeter calculation:

:contentReference[oaicite:5]{index=5}

---

# Internal Working

Interface provides:
```text
common structure
```

Classes provide:
```text
different implementations
```

This demonstrates:
```text
abstraction and polymorphism
```

---

# Time Complexity

Each operation:

:contentReference[oaicite:6]{index=6}

---

# Space Complexity

:contentReference[oaicite:7]{index=7}

---

# Advantages of Interface

- Supports abstraction
- Improves flexibility
- Promotes code reusability
- Supports multiple inheritance

---

# Limitations

- Cannot create object of interface
- Interface methods are abstract by default

---

# Edge Cases

## Case 1: Radius = 0

Area:

:contentReference[oaicite:8]{index=8}

---

## Case 2: Invalid Choice

Program prints:
```text
Invalid choice!
```

---

## Case 3: Negative Dimensions

Program still calculates mathematically.

---

# Possible Improvements

- Add more shapes
- Add validation
- Use abstract class

---

# Possible Errors

## 1. InputMismatchException

Occurs when invalid datatype entered.

---

## 2. Invalid Choice

Occurs when unsupported option selected.

---

# Viva Questions

## Q1. What is interface?
Blueprint containing abstract methods.

---

## Q2. Which keyword is used to implement interface?

```java
implements
```

---

## Q3. Can interface contain variables?
Yes, public static final variables.

---

## Q4. Can we create object of interface?
No.

---

## Q5. What is abstraction?
Hiding implementation details.

---

## Q6. What is method overriding?
Providing implementation for inherited methods.

---

## Q7. Which loop is used here?
do-while loop.

---

## Q8. Which statement is used for menu?
switch-case.

---

## Q9. What is polymorphism?
Ability of method to behave differently.

---

## Q10. What is time complexity?

:contentReference[oaicite:9]{index=9}