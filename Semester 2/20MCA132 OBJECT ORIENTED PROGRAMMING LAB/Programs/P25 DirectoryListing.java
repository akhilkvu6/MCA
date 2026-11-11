import java.io.File;
import java.util.Scanner;

public class P25_DirectoryListing
{
    static boolean found=false;

    static void listFilesAndDirectories(File directory)
    {
        File[] fileList=directory.listFiles();

        if(fileList!=null)
        {
            for(File file:fileList)
            {
                System.out.println(file.getName());

                if(file.isDirectory())
                {
                    listFilesAndDirectories(file);
                }
            }
        }
    }

    static void searchFile(File directory,String fileName)
    {
        File[] fileList=directory.listFiles();

        if(fileList!=null)
        {
            for(File file:fileList)
            {
                if(file.isFile() && file.getName().equals(fileName))
                {
                    System.out.println("File found at: "+file.getAbsolutePath());

                    found=true;
                }

                else if(file.isDirectory())
                {
                    searchFile(file,fileName);
                }
            }
        }
    }

    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);

        System.out.print("Enter the directory path: ");

        String directoryPath=scanner.nextLine();

        File directory=new File(directoryPath);

        if(directory.exists() && directory.isDirectory())
        {
            System.out.println("Files and directories in the specified directory:");

            listFilesAndDirectories(directory);

            System.out.print("\nEnter the file name to search: ");

            String fileName=scanner.nextLine();

            System.out.println("Searching for file '"+fileName+"'...");

            searchFile(directory,fileName);

            if(!found)
            {
                System.out.println("File '"+fileName+"' not found.");
            }
        }

        else
        {
            System.out.println("Invalid directory path.");
        }

        scanner.close();
    }
}