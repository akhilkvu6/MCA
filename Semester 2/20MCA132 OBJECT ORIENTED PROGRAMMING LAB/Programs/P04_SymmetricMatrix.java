// Program 4: Read a matrix from the console and check whether it is symmetric or not.

import java.util.Scanner;

class Symmetric
{
    Scanner sc = new Scanner(System.in);

    int rows, columns;
    int matrix[][];
    int flag = 0;

    Symmetric()
    {
        System.out.print("Enter size of matrix: ");
        rows = sc.nextInt();
        columns = sc.nextInt();

        matrix = new int[rows][columns];

        System.out.println("Enter value of matrix: ");

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                matrix[i][j] = sc.nextInt();
            }
        }
    }

    void transpose()
    {
        if(rows != columns)
        {
            System.out.println("Matrix is not symmetric");
            return;
        }

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                if(matrix[j][i] != matrix[i][j])
                {
                    flag = 1;
                    break;
                }
            }
        }

        if(flag != 1)
        {
            System.out.println("Matrix is symmetric");
        }
        else
        {
            System.out.println("Matrix is not symmetric");
        }
    }
}

public class P4_SymmetricMatrix
{
    public static void main(String[] args)
    {
        Symmetric a = new Symmetric();

        a.transpose();
    }
}