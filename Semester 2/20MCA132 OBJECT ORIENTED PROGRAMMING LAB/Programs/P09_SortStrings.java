// Program 9: Sort strings using Bubble Sort.

import java.util.Scanner;

class SortStrings
{
    Scanner sc = new Scanner(System.in);

    String s[];
    int size;

    SortStrings()
    {
        System.out.print("Enter no: of strings: ");
        size = sc.nextInt();

        s = new String[size];

        System.out.println("Enter " + size + " strings:");

        for(int i = 0; i < size; i++)
        {
            s[i] = sc.next();
        }
    }

    void sort()
    {
        for(int i = 0; i < size; i++)
        {
            for(int j = 0; j < size - i - 1; j++)
            {
                if(s[j].compareTo(s[j + 1]) > 0)
                {
                    String temp = s[j];

                    s[j] = s[j + 1];

                    s[j + 1] = temp;
                }
            }
        }
    }

    void display()
    {
        for(int i = 0; i < size; i++)
        {
            System.out.print(s[i] + " ");
        }
    }
}

public class P09_SortStrings
{
    public static void main(String[] args)
    {
        SortStrings s1 = new SortStrings();

        System.out.println("\nOriginal String Array");
        s1.display();

        s1.sort();

        System.out.println("\n\nSorted String Array");
        s1.display();
    }
}