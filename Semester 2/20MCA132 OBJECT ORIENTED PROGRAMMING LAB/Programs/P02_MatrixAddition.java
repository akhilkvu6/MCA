// Program 2: Read 2 matrices from the console and perform matrix addition.

import java.util.Scanner;

class AddMatrix
{
    Scanner sc = new Scanner(System.in);

    int rows, columns;
    int matrix[][];

    AddMatrix(int n)
    {
        System.out.print("Enter size of matrix " + n + ": ");
        rows = sc.nextInt();
        columns = sc.nextInt();

        matrix = new int[rows][columns];

        System.out.println("Enter value of matrix " + n + ": ");

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                matrix[i][j] = sc.nextInt();
            }
        }
    }

    void add(AddMatrix b)
    {
        if(rows != b.rows || columns != b.columns)
        {
            System.out.println("Addition of matrix not possible");
        }
        else
        {
            for(int i = 0; i < rows; i++)
            {
                for(int j = 0; j < columns; j++)
                {
                    matrix[i][j] += b.matrix[i][j];
                }
            }

            System.out.println("Sum of matrix:");
            this.display();
        }
    }

    void display()
    {
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                System.out.print(matrix[i][j] + " ");
            }

            System.out.println();
        }
    }
}

public class P02_MatrixAddition
{
    public static void main(String[] args)
    {
        AddMatrix a = new AddMatrix(1);
        AddMatrix b = new AddMatrix(2);

        a.add(b);
    }
}