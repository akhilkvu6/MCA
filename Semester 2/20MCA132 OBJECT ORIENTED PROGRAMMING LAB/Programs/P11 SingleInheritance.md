# Program 11 - Single Inheritance

## Question

Create a class `Employee` with data members:
- Empid
- Name
- Salary
- Address

Create another class `Teacher` that inherits the properties of class `Employee` and contains:
- Department
- Subjects taught

Use array of objects to display details of N teachers.

---

# Filename

```text
P11_SingleInheritance.java
```

---

# Source Code

```java
// Program 11: Single Inheritance using Employee and Teacher classes.

import java.util.Scanner;

class Employee
{
    Scanner sc = new Scanner(System.in);

    int empId;
    String name, address;
    double salary;

    Employee(int x)
    {
        System.out.println("\nEnter Details of Teacher " + x);

        System.out.print("Enter Employee Id: ");
        empId = sc.nextInt();

        System.out.print("Enter Employee Name: ");
        name = sc.next();

        System.out.print("Enter Salary: ");
        salary = sc.nextDouble();

        System.out.print("Enter Address: ");
        address = sc.next();
    }
}

class Teacher extends Employee
{
    Scanner sc = new Scanner(System.in);

    String dept;
    String subject[];

    int no;

    Teacher(int x)
    {
        super(x);

        System.out.print("Enter Department: ");
        dept = sc.next();

        System.out.print("Enter no: of subjects taught: ");
        no = sc.nextInt();

        subject = new String[no];

        System.out.println("Enter list of subjects:");

        for(int i = 0; i < no; i++)
        {
            subject[i] = sc.next();
        }
    }

    void display(int j)
    {
        System.out.println("\nTeacher " + j + " Details");

        System.out.println("Employee Id: " + empId);

        System.out.println("Employee Name: " + name);

        System.out.println("Salary: " + salary);

        System.out.println("Address: " + address);

        System.out.println("Department: " + dept);

        System.out.print("Subjects: ");

        for(int i = 0; i < no; i++)
        {
            System.out.print(subject[i] + " ");
        }

        System.out.println();
    }
}

public class P11_SingleInheritance
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter no: of teachers: ");
        int n = sc.nextInt();

        Teacher t[] = new Teacher[n];

        for(int i = 0; i < n; i++)
        {
            t[i] = new Teacher(i + 1);
        }

        for(int i = 0; i < n; i++)
        {
            t[i].display(i + 1);
        }
    }
}
```

---

# Concepts Used

- Inheritance
- Single Inheritance
- Super Class
- Sub Class
- Constructor
- super Keyword
- Array of Objects
- Scanner Class
- Method

---

# Theory

Inheritance is one of the important features of:
```text
Object Oriented Programming (OOP)
```

Inheritance allows:
```text
one class to acquire properties and methods of another class
```

---

# Single Inheritance

Single inheritance means:
```text
one child class inherits one parent class
```

In this program:

```text
Teacher → Child Class
Employee → Parent Class
```

---

# Class Hierarchy

```text
Employee
    ↑
Teacher
```

Teacher class inherits:
- employee id
- name
- salary
- address

from Employee class.

---

# Employee Class

The Employee class contains:
- empId
- name
- salary
- address

It acts as:
```text
base class / super class
```

---

# Teacher Class

Teacher class extends Employee class using:

```java
class Teacher extends Employee
```

Teacher contains additional details:
- department
- subjects taught

---

# super Keyword

```java
super(x);
```

Used to call:
```text
parent class constructor
```

This initializes inherited variables.

---

# Array of Objects

```java
Teacher t[] = new Teacher[n];
```

Used to store multiple teacher objects.

---

# Subject Array

```java
String subject[];
```

Stores list of subjects taught by teacher.

---

# Constructor

Constructor automatically initializes:
- employee details
- teacher details

during object creation.

---

# Detailed Algorithm

1. Create class:
```java
Employee
```

2. Declare:
- empId
- name
- salary
- address

3. Create Employee constructor.

4. Create class:
```java
Teacher
```

5. Inherit Employee using:
```java
extends
```

6. Declare:
- department
- subject array
- number of subjects

7. Create Teacher constructor.

8. Use:
```java
super(x)
```

to call Employee constructor.

9. Read teacher details.

10. Create:
```java
display()
```

method.

11. In main method:
   - read number of teachers

12. Create array:
```java
Teacher t[]
```

13. Create teacher objects using loop.

14. Display teacher details.

15. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Number of Teachers
   ↓
Create Teacher Array
   ↓
Call Employee Constructor
   ↓
Call Teacher Constructor
   ↓
Store Details
   ↓
Display Teacher Information
   ↓
Stop
```

---

# Sample Input

```text
Enter no: of teachers: 1

Enter Details of Teacher 1

Enter Employee Id: 101

Enter Employee Name: Akhil

Enter Salary: 50000

Enter Address: TVM

Enter Department: MCA

Enter no: of subjects taught: 2

Enter list of subjects:
Java
Python
```

---

# Sample Output

```text
Teacher 1 Details

Employee Id: 101

Employee Name: Akhil

Salary: 50000.0

Address: TVM

Department: MCA

Subjects: Java Python
```

---

# Dry Run

Teacher Object Created:

```java
Teacher t1 = new Teacher(1);
```

---

# Step 1

Teacher constructor called.

---

# Step 2

```java
super(1);
```

calls Employee constructor.

---

# Step 3

Employee details initialized.

---

# Step 4

Teacher-specific details initialized.

---

# Step 5

display() prints all details.

---

# Internal Working

Memory contains:
- inherited variables from Employee
- own variables of Teacher

Teacher object accesses:
```text
both parent and child members
```

---

# Time Complexity

Input and display operations:

:contentReference[oaicite:0]{index=0}

where:
```text
n = number of teachers
```

---

# Space Complexity

:contentReference[oaicite:1]{index=1}

because array of teacher objects is used.

---

# Advantages of Inheritance

- Code reusability
- Reduced redundancy
- Better organization
- Easy maintenance

---

# Limitations

- Tight coupling between classes
- Complex hierarchy may become difficult

---

# Edge Cases

## Case 1: Zero Teachers

Input:
```text
0
```

No objects created.

---

## Case 2: Zero Subjects

Teacher will have empty subject list.

---

## Case 3: Large Number of Teachers

Consumes more memory.

---

# Possible Improvements

- Use ArrayList
- Add getter/setter methods
- Add multiple inheritance concepts through interfaces

---

# Possible Errors

## 1. InputMismatchException

Occurs when invalid datatype entered.

---

## 2. NullPointerException

Occurs if objects not initialized.

---

## 3. ArrayIndexOutOfBoundsException

Occurs if subject array exceeds size.

---

# Viva Questions

## Q1. What is inheritance?
Acquiring properties of another class.

---

## Q2. What is single inheritance?
One child inherits one parent.

---

## Q3. Which keyword is used for inheritance?

```java
extends
```

---

## Q4. What is super keyword used for?
Calling parent class constructor or methods.

---

## Q5. What is parent class here?
Employee.

---

## Q6. What is child class here?
Teacher.

---

## Q7. What is constructor?
Special method used for initialization.

---

## Q8. What is array of objects?
Array storing object references.

---

## Q9. Can child class access parent variables?
Yes.

---

## Q10. What is the benefit of inheritance?
Code reusability.