# Program 5 - Inner Class

## Question

Create CPU with attribute `price`. Create inner class `Processor` (number of cores, manufacturer) and static nested class `RAM` (memory, manufacturer). Create an object of CPU and print information of Processor and RAM.

---

# Filename

```text
P5_InnerClass.java
```

---

# Source Code

```java
// Program 5: Create CPU with attribute price. Create inner class Processor and static nested class RAM.

import java.util.Scanner;

class CPU
{
    Scanner sc = new Scanner(System.in);

    int price;

    class Processor
    {
        int noOfCores;
        String manufacturer;

        Processor()
        {
            System.out.print("Enter number of cores in the processor: ");
            noOfCores = sc.nextInt();

            System.out.print("Enter manufacturer of the processor: ");
            manufacturer = sc.next();
        }
    }

    static class RAM
    {
        Scanner sc = new Scanner(System.in);

        int memory;
        String manufacturer;

        RAM()
        {
            System.out.print("Enter memory capacity of RAM: ");
            memory = sc.nextInt();

            System.out.print("Enter manufacturer of the RAM: ");
            manufacturer = sc.next();
        }
    }
}

public class P5_InnerClass
{
    public static void main(String[] args)
    {
        CPU c = new CPU();

        CPU.Processor p = c.new Processor();

        CPU.RAM r = new CPU.RAM();

        c.price = 2500 + (p.noOfCores * 20) + (r.memory * 15);

        System.out.println("\nProcessor Details");
        System.out.println("Number of Cores: " + p.noOfCores);
        System.out.println("Manufacturer: " + p.manufacturer);

        System.out.println("\nRAM Details");
        System.out.println("Memory Capacity: " + r.memory + " GB");
        System.out.println("Manufacturer: " + r.manufacturer);

        System.out.println("\nCPU Price: " + c.price);
    }
}
```

---

# Concepts Used

- Class
- Object
- Inner Class
- Static Nested Class
- Constructor
- Scanner Class
- Encapsulation
- Object Creation
- Static Members

---

# Theory

Java supports:
- inner classes
- nested classes

These classes help logically group related classes together.

---

# Inner Class

An inner class is a class defined inside another class.

Example:
```java
class Processor
```

inside:
```java
class CPU
```

Inner classes:
- can access outer class members directly
- require outer class object for creation

Creation syntax:
```java
CPU.Processor p = c.new Processor();
```

---

# Static Nested Class

A static nested class is declared using:
```java
static class RAM
```

Static nested classes:
- belong to outer class
- do not require outer class object
- behave similar to static members

Creation syntax:
```java
CPU.RAM r = new CPU.RAM();
```

---

# Detailed Explanation

## CPU Class

The `CPU` class contains:
- CPU price
- inner class `Processor`
- static nested class `RAM`

---

# Instance Variable

```java
int price;
```

Stores CPU price.

---

# Processor Inner Class

```java
class Processor
```

Stores:
- number of cores
- processor manufacturer

---

# Processor Variables

```java
int noOfCores;
String manufacturer;
```

| Variable | Description |
|---|---|
| `noOfCores` | Number of processor cores |
| `manufacturer` | Processor company name |

---

# RAM Static Nested Class

```java
static class RAM
```

Stores:
- RAM memory
- RAM manufacturer

---

# RAM Variables

```java
int memory;
String manufacturer;
```

| Variable | Description |
|---|---|
| `memory` | RAM size |
| `manufacturer` | RAM company name |

---

# Constructor Usage

Constructors are used to:
- read input
- initialize variables

---

# CPU Price Calculation

```java
c.price = 2500 + (p.noOfCores * 20) + (r.memory * 15);
```

Formula:
- base CPU price = 2500
- each processor core adds 20
- each GB RAM adds 15

---

# Detailed Algorithm

1. Create class named `CPU`.

2. Declare variable:
```java
price
```

3. Create inner class:
```java
Processor
```

4. Declare variables:
   - `noOfCores`
   - `manufacturer`

5. Create constructor for Processor class.

6. Read:
   - number of cores
   - processor manufacturer

7. Create static nested class:
```java
RAM
```

8. Declare variables:
   - `memory`
   - `manufacturer`

9. Create constructor for RAM class.

10. Read:
   - RAM memory
   - RAM manufacturer

11. Create object:
```java
CPU c
```

12. Create Processor object using:
```java
CPU.Processor p = c.new Processor();
```

13. Create RAM object using:
```java
CPU.RAM r = new CPU.RAM();
```

14. Calculate CPU price.

15. Display:
   - processor details
   - RAM details
   - CPU price

16. Stop program.

---

# Flow of Execution

```text
Start Program
      ↓
Create CPU Object
      ↓
Create Processor Object
      ↓
Read Processor Details
      ↓
Create RAM Object
      ↓
Read RAM Details
      ↓
Calculate CPU Price
      ↓
Display Processor Details
      ↓
Display RAM Details
      ↓
Display CPU Price
      ↓
Stop Program
```

---

# Dry Run

Suppose:

## Processor

```text
Cores = 4
Manufacturer = Intel
```

## RAM

```text
Memory = 8 GB
Manufacturer = Kingston
```

---

# CPU Price Calculation

```text
2500 + (4 × 20) + (8 × 15)
```

---

# Step 1

Processor contribution:

:contentReference[oaicite:0]{index=0}

---

# Step 2

RAM contribution:

:contentReference[oaicite:1]{index=1}

---

# Step 3

Total price:

:contentReference[oaicite:2]{index=2}

---

# Sample Input

```text
Enter number of cores in the processor: 4
Enter manufacturer of the processor: Intel

Enter memory capacity of RAM: 8
Enter manufacturer of the RAM: Kingston
```

---

# Sample Output

```text
Processor Details
Number of Cores: 4
Manufacturer: Intel

RAM Details
Memory Capacity: 8 GB
Manufacturer: Kingston

CPU Price: 2700
```

---

# Internal Working

## Processor Object Creation

```java
CPU.Processor p = c.new Processor();
```

Requires CPU object because:
- Processor is non-static inner class.

---

## RAM Object Creation

```java
CPU.RAM r = new CPU.RAM();
```

Does not require CPU object because:
- RAM is static nested class.

---

# Edge Cases

## Case 1: Zero RAM

Input:
```text
RAM = 0
```

Program still calculates price.

---

## Case 2: Large Core Count

Input:
```text
32 cores
```

Program still works correctly.

---

# Limitations

Current program:
- uses simple price formula
- handles only integer values
- does not validate inputs

---

# Possible Improvements

- Add CPU model
- Add RAM type
- Use floating point pricing
- Add GPU details
- Add separate display methods

---

# Time Complexity

:contentReference[oaicite:3]{index=3}

because only constant operations are performed.

---

# Space Complexity

:contentReference[oaicite:4]{index=4}

because only fixed variables are used.

---

# Possible Errors

## 1. InputMismatchException

Occurs when non-integer value is entered.

Example:
```text
abc
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

## 3. Incorrect Inner Class Object Creation

Wrong:
```java
new Processor();
```

Correct:
```java
c.new Processor();
```

because Processor is non-static inner class.

---

# Viva Questions

## Q1. What is an inner class?
Class defined inside another class.

---

## Q2. What is static nested class?
Nested class declared using static keyword.

---

## Q3. Difference between inner class and static nested class?

| Inner Class | Static Nested Class |
|---|---|
| Requires outer object | Does not require outer object |
| Can access outer members directly | Behaves like static member |

---

## Q4. Why use inner classes?
To logically group related classes.

---

## Q5. Why use static nested class?
When nested class does not depend on outer object.

---

## Q6. How is Processor object created?

```java
CPU.Processor p = c.new Processor();
```

---

## Q7. How is RAM object created?

```java
CPU.RAM r = new CPU.RAM();
```

---

## Q8. What is encapsulation?
Combining variables and methods inside class.

---

## Q9. What is constructor?
Special method automatically called during object creation.

---

## Q10. What is time complexity?

:contentReference[oaicite:5]{index=5}