import java.io.*;
import java.util.*;

public class P28_EvenOddFiles
{
    public static void main(String[] args)
    {
        try
        {
            Scanner sc=new Scanner(System.in);

            System.out.print("Enter source file name: ");
            String source=sc.nextLine();

            Scanner fileScanner=new Scanner(new File(source));

            FileWriter evenFile=new FileWriter("even.txt");

            FileWriter oddFile=new FileWriter("odd.txt");

            while(fileScanner.hasNextInt())
            {
                int num=fileScanner.nextInt();

                if(num%2==0)
                {
                    evenFile.write(num+" ");
                }

                else
                {
                    oddFile.write(num+" ");
                }
            }

            evenFile.close();

            oddFile.close();

            fileScanner.close();

            sc.close();

            System.out.println("Even numbers copied to even.txt");

            System.out.println("Odd numbers copied to odd.txt");
        }

        catch(IOException e)
        {
            System.out.println("Error: "+e.getMessage());
        }
    }
}