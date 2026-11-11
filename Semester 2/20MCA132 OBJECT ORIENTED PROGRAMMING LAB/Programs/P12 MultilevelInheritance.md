# Program 12 - Multilevel Inheritance

## Question

Create a class `Person` with data members:
- Name
- Gender
- Address
- Age

Create another class `Employee` that inherits `Person` and contains:
- Employee ID
- Company Name
- Qualification
- Salary

Create another class `Teacher` that inherits `Employee` and contains:
- Subject
- Department
- Teacher ID

Use array of objects to display details of N teachers.

---

# Filename

```text
P12_MultilevelInheritance.java
```

---

# Source Code

```java
// Program 12: Multilevel Inheritance using Person, Employee and Teacher classes.

import java.util.Scanner;

class Person
{
    Scanner sc = new Scanner(System.in);

    String name, address;
    char gender;
    int age;

    Person(int x)
    {
        System.out.println("\nEnter Details of Teacher " + x);

        System.out.print("Enter Name: ");
        name = sc.next();

        System.out.print("Enter Gender (M/F/O): ");
        gender = sc.next().charAt(0);

        System.out.print("Enter Age: ");
        age = sc.nextInt();

        System.out.print("Enter Address: ");
        address = sc.next();
    }
}

class Employee extends Person
{
    Scanner sc = new Scanner(System.in);

    int empId;

    String companyName, qualification;

    double salary;

    Employee(int x)
    {
        super(x);

        System.out.print("Enter Employee ID: ");
        empId = sc.nextInt();

        System.out.print("Enter Company Name: ");
        companyName = sc.next();

        System.out.print("Enter Qualification: ");
        qualification = sc.next();

        System.out.print("Enter Salary: ");
        salary = sc.nextDouble();
    }
}

class Teacher extends Employee
{
    Scanner sc = new Scanner(System.in);

    String subject, department;

    int teacherId;

    Teacher(int x)
    {
        super(x);

        System.out.print("Enter Teacher ID: ");
        teacherId = sc.nextInt();

        System.out.print("Enter Subject: ");
        subject = sc.next();

        System.out.print("Enter Department: ");
        department = sc.next();
    }

    void display(int n)
    {
        System.out.println("\nTeacher " + n + " Details");

        System.out.println("Name: " + name);

        System.out.println("Gender: " + gender);

        System.out.println("Address: " + address);

        System.out.println("Age: " + age);

        System.out.println("Employee ID: " + empId);

        System.out.println("Teacher ID: " + teacherId);

        System.out.println("Company Name: " + companyName);

        System.out.println("Department: " + department);

        System.out.println("Qualification: " + qualification);

        System.out.println("Salary: " + salary);

        System.out.println("Subject: " + subject);
    }
}

public class P12_MultilevelInheritance
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
- Multilevel Inheritance
- Constructor
- super Keyword
- Array of Objects
- Method
- Scanner Class
- Object Oriented Programming

---

# Theory

Inheritance allows:
```text
one class to acquire properties and methods of another class
```

This program demonstrates:
```text
Multilevel Inheritance
```

---

# Multilevel Inheritance

Multilevel inheritance means:
```text
a class inherits another class,
which itself inherits another class
```

---

# Class Hierarchy

```text
Person
   ↑
Employee
   ↑
Teacher
```

---

# Person Class

Contains:
- name
- gender
- address
- age

Acts as:
```text
base class
```

---

# Employee Class

Employee inherits:
```text
Person
```

Additional members:
- employee ID
- company name
- qualification
- salary

---

# Teacher Class

Teacher inherits:
```text
Employee
```

Additional members:
- teacher ID
- department
- subject

---

# super Keyword

```java
super(x);
```

Used to call:
```text
parent class constructor
```

This initializes inherited data members.

---

# Constructor Chain

When Teacher object is created:

```text
Teacher Constructor
     ↓
Employee Constructor
     ↓
Person Constructor
```

This process is called:
```text
constructor chaining
```

---

# Array of Objects

```java
Teacher t[] = new Teacher[n];
```

Stores multiple Teacher objects.

---

# Detailed Algorithm

1. Create class:
```java
Person
```

2. Declare:
- name
- gender
- age
- address

3. Create constructor for Person.

4. Create class:
```java
Employee
```

5. Inherit:
```java
Person
```

6. Declare:
- employee ID
- company name
- qualification
- salary

7. Create Employee constructor.

8. Use:
```java
super(x)
```

9. Create class:
```java
Teacher
```

10. Inherit:
```java
Employee
```

11. Declare:
- teacher ID
- department
- subject

12. Create Teacher constructor.

13. Create:
```java
display()
```

method.

14. Read number of teachers.

15. Create Teacher array.

16. Create Teacher objects.

17. Display teacher details.

18. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Number of Teachers
   ↓
Create Teacher Array
   ↓
Call Person Constructor
   ↓
Call Employee Constructor
   ↓
Call Teacher Constructor
   ↓
Store Data
   ↓
Display Teacher Details
   ↓
Stop
```

---

# Sample Input

```text
Enter no: of teachers: 1

Enter Name: Akhil

Enter Gender (M/F/O): M

Enter Age: 22

Enter Address: TVM

Enter Employee ID: 101

Enter Company Name: CET

Enter Qualification: MCA

Enter Salary: 50000

Enter Teacher ID: 201

Enter Subject: Java

Enter Department: MCA
```

---

# Sample Output

```text
Teacher 1 Details

Name: Akhil

Gender: M

Address: TVM

Age: 22

Employee ID: 101

Teacher ID: 201

Company Name: CET

Department: MCA

Qualification: MCA

Salary: 50000.0

Subject: Java
```

---

# Dry Run

Teacher object created:

```java
Teacher t1 = new Teacher(1);
```

---

# Step 1

Teacher constructor executes.

---

# Step 2

```java
super(x);
```

calls Employee constructor.

---

# Step 3

Employee constructor calls:
```java
super(x);
```

which calls Person constructor.

---

# Step 4

Person data initialized.

---

# Step 5

Employee data initialized.

---

# Step 6

Teacher data initialized.

---

# Step 7

display() prints all details.

---

# Internal Working

Teacher object contains:
- Person variables
- Employee variables
- Teacher variables

This demonstrates:
```text
inheritance hierarchy
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

for storing teacher objects.

---

# Advantages of Multilevel Inheritance

- Code reusability
- Better organization
- Reduced redundancy
- Hierarchical representation

---

# Limitations

- Complex inheritance chain
- Difficult debugging in large systems

---

# Edge Cases

## Case 1: No Teachers

Input:
```text
0
```

No objects created.

---

## Case 2: Invalid Age

Negative age accepted unless validated.

---

## Case 3: Empty Strings

May produce incomplete output.

---

# Possible Improvements

- Add validation
- Use getter/setter methods
- Use ArrayList
- Add menu-driven operations

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. NullPointerException

Occurs if objects not initialized.

---

## 3. ArrayIndexOutOfBoundsException

Occurs if array index exceeds size.

---

# Viva Questions

## Q1. What is inheritance?
Acquiring properties of another class.

---

## Q2. What is multilevel inheritance?
Inheritance across multiple levels.

---

## Q3. Which keyword is used for inheritance?

```java
extends
```

---

## Q4. What is constructor chaining?
Calling constructors in inheritance hierarchy.

---

## Q5. What is super keyword used for?
Calling parent constructor or methods.

---

## Q6. Which class is base class here?
Person.

---

## Q7. Which class is intermediate class?
Employee.

---

## Q8. Which class is derived class?
Teacher.

---

## Q9. What is array of objects?
Array storing object references.

---

## Q10. Advantage of inheritance?
Code reusability.