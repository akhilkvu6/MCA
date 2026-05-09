import java.io.*;

public class P26_WriteRead
{
    public static void main(String[] args)
    {
        try
        {
            FileOutputStream fout=new FileOutputStream("data.txt");
            String data="This is the implementation of write and read operation";
            byte[] b=data.getBytes();

            fout.write(b);
            fout.close();

            FileInputStream fin=new FileInputStream("data.txt");

            int ch;

            while((ch=fin.read())!=-1)
            {
                System.out.print((char)ch);
            }

            fin.close();
        }

        catch(IOException e)
        {
            System.out.println(e);
        }
    }
}