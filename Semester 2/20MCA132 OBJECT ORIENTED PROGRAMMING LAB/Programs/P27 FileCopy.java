import java.io.*;
import java.util.Scanner;

public class P27_FileCopy
{
    public static void main(String args[])
    {
        try
        {
            Scanner sc=new Scanner(System.in);

            System.out.print("Enter the source file path: ");
            String source=sc.nextLine();

            System.out.print("Enter the destination file path: ");
            String destination=sc.nextLine();

            FileReader f1=new FileReader(source);

            FileWriter f2=new FileWriter(destination);

            int ch;

            while((ch=f1.read())!=-1)
            {
                f2.write(ch);
            }

            f1.close();

            f2.close();

            sc.close();

            System.out.println("File copied successfully.");
        }

        catch(IOException e)
        {
            System.out.println("Error occurred: "+e.getMessage());
        }
    }
}