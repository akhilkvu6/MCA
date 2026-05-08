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