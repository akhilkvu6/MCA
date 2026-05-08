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