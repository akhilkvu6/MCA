// Program 6: Program to search for an element in an array.

import java.util.Scanner;

class Array
{
    Scanner sc = new Scanner(System.in);

    int arr[], size;

    Array(int n)
    {
        size = n;

        arr = new int[n];

        System.out.println("Enter elements to the array:");

        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
    }

    void search(int n)
    {
        int flag = 0;

        for(int i = 0; i < size; i++)
        {
            if(arr[i] == n)
            {
                flag = 1;

                System.out.println(n + " is found in the array.");

                break;
            }
        }

        if(flag == 0)
        {
            System.out.println(n + " is not an element of the array.");
        }
    }
}

public class P6_SearchElementInArray
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter no: of elements in the array: ");
        int n = sc.nextInt();

        Array a = new Array(n);

        System.out.print("Enter number to be searched: ");
        int num = sc.nextInt();

        a.search(num);
    }
}