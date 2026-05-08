# Program 8 - Array Of Objects

## Question

Program to create a class for Employee having attributes:
- eNo
- eName
- eSalary

Read employee information and search for an employee using employee number using the concept of Array of Objects.

---

# Filename

```text
P8_ArrayOfObjects.java
```

---

# Source Code

```java
// Program 8: Array of Objects - Employee Search.

import java.util.Scanner;

class Employee
{
    Scanner sc = new Scanner(System.in);

    int eNo;
    String eName;
    double eSalary;

    Employee(int n)
    {
        System.out.println("\nEnter Details for Employee " + n);

        System.out.print("Enter Employee Number: ");
        eNo = sc.nextInt();

        System.out.print("Enter Employee Name: ");
        eName = sc.next();

        System.out.print("Enter Employee Salary: ");
        eSalary = sc.nextDouble();
    }
}

public class P8_ArrayOfObjects
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of employees: ");
        int n = sc.nextInt();

        Employee e[] = new Employee[n];

        for(int i = 0; i < n; i++)
        {
            e[i] = new Employee(i + 1);
        }

        System.out.print("\nEnter Employee Number to search: ");
        int num = sc.nextInt();

        int flag = 0;

        for(int i = 0; i < n; i++)
        {
            if(e[i].eNo == num)
            {
                System.out.println("\nEmployee Name: " + e[i].eName);

                System.out.println("Employee Salary: " + e[i].eSalary);

                flag = 1;

                break;
            }
        }

        if(flag == 0)
        {
            System.out.println("Employee Not Registered!!!");
        }
    }
}
```

---

# Concepts Used

- Class
- Object
- Constructor
- Array of Objects
- Linear Search
- Looping
- Conditional Statements
- Scanner Class

---

# Theory

An array of objects is an array where each element stores:
```text
reference to an object
```

Instead of storing primitive values like:
- int
- float
- char

it stores:
- objects

This program uses:
```text
Array of Employee Objects
```

to store multiple employee records.

---

# Employee Class

The `Employee` class contains:
- employee number
- employee name
- employee salary

Each object represents:
```text
one employee
```

---

# Instance Variables

```java
int eNo;
String eName;
double eSalary;
```

| Variable | Purpose |
|---|---|
| `eNo` | Employee Number |
| `eName` | Employee Name |
| `eSalary` | Employee Salary |

---

# Constructor

```java
Employee(int n)
```

Constructor automatically:
- reads employee details
- initializes employee object

---

# Array of Objects

```java
Employee e[] = new Employee[n];
```

Creates array capable of storing:
```text
n employee objects
```

Initially:
- all elements contain null references

---

# Object Creation Inside Loop

```java
e[i] = new Employee(i + 1);
```

Creates actual Employee objects.

---

# Searching Logic

Program searches employee using:
```text
employee number
```

using:
```java
if(e[i].eNo == num)
```

---

# Flag Variable

```java
int flag = 0;
```

Used to check:
- employee found
- employee not found

---

# break Statement

```java
break;
```

Stops searching once employee is found.

Improves efficiency.

---

# Detailed Algorithm

1. Create class:
```java
Employee
```

2. Declare variables:
- eNo
- eName
- eSalary

3. Create constructor:
```java
Employee(int n)
```

4. Read employee details.

5. In main method:
   - read number of employees

6. Create array:
```java
Employee e[]
```

7. Use loop to create employee objects.

8. Read employee number to search.

9. Traverse array using loop.

10. Compare:
```java
e[i].eNo
```

with:
```java
num
```

11. If found:
   - display employee details
   - set flag = 1
   - stop loop

12. If flag remains 0:
   - display:
```text
Employee Not Registered!!!
```

13. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Number of Employees
   ↓
Create Employee Array
   ↓
Read Employee Details
   ↓
Read Employee Number to Search
   ↓
Search Employee
   ↓
Employee Found?
   ↓
Display Result
   ↓
Stop
```

---

# Dry Run

Suppose:

| Employee No | Name | Salary |
|---|---|---|
| 101 | Akhil | 50000 |
| 102 | Rahul | 45000 |

Search:
```text
102
```

---

# Step 1

Check:
```text
101 == 102
```

False.

---

# Step 2

Check:
```text
102 == 102
```

True.

---

# Output

```text
Employee Name: Rahul
Employee Salary: 45000
```

---

# Sample Input

```text
Enter number of employees: 2

Enter Details for Employee 1
Enter Employee Number: 101
Enter Employee Name: Akhil
Enter Employee Salary: 50000

Enter Details for Employee 2
Enter Employee Number: 102
Enter Employee Name: Rahul
Enter Employee Salary: 45000

Enter Employee Number to search: 102
```

---

# Sample Output

```text
Employee Name: Rahul
Employee Salary: 45000.0
```

---

# Edge Cases

## Case 1: Employee Not Found

Input:
```text
999
```

Output:
```text
Employee Not Registered!!!
```

---

## Case 2: Duplicate Employee Numbers

Program returns:
```text
first matching employee
```

---

## Case 3: Zero Employees

Input:
```text
0
```

Creates empty employee array.

---

# Internal Working

Array stores:
```text
references to Employee objects
```

Each object contains:
- employee number
- employee name
- employee salary

Searching performed using:
```text
Linear Search
```

---

# Time Complexity

Worst Case:

:contentReference[oaicite:0]{index=0}

because every employee may need checking.

---

# Best Case Complexity

If employee found at beginning:

:contentReference[oaicite:1]{index=1}

---

# Space Complexity

:contentReference[oaicite:2]{index=2}

for storing employee objects.

---

# Advantages

- Easy storage of multiple objects
- Better organization of data
- Demonstrates object-oriented programming

---

# Limitations

- Uses linear search
- No sorting
- No duplicate checking

---

# Possible Improvements

- Add sorting
- Add binary search
- Add employee update/delete
- Use ArrayList instead of array

---

# Possible Errors

## 1. InputMismatchException

Occurs when invalid datatype entered.

Example:
```text
abc
```

instead of integer salary.

---

## 2. NullPointerException

Occurs if object not initialized properly.

---

## 3. ArrayIndexOutOfBoundsException

Occurs if array index exceeds limit.

---

# Viva Questions

## Q1. What is an array of objects?
Array storing references to objects.

---

## Q2. What is constructor?
Special method automatically called during object creation.

---

## Q3. Why use array of objects?
To store multiple objects efficiently.

---

## Q4. Which searching method is used?
Linear Search.

---

## Q5. What is object reference?
Memory address of object.

---

## Q6. What is Scanner class?
Class used for user input.

---

## Q7. What is time complexity of linear search?

:contentReference[oaicite:3]{index=3}

---

## Q8. What is break statement?
Terminates loop immediately.

---

## Q9. What is null reference?
Reference variable not pointing to object.

---

## Q10. Difference between primitive array and object array?

| Primitive Array | Object Array |
|---|---|
| Stores values | Stores object references |
| int[] | Employee[] |