# Program 25 - Subdirectories and Files

## Question

Program to list the subdirectories and files in a given directory and also search for a file name.

---

# Filename

```text
P25_DirectoryListing.java
```

---

# Source Code

```java
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
```

---

# Concepts Used

- File Handling
- File Class
- Directories and Files
- Recursive Functions
- Searching Files
- Scanner Class
- Java IO Package

---

# Theory

Java provides:
```java
File
```

class in:
```java
java.io
```

package for:
- file handling
- directory handling
- file searching

---

# File Class

```java
File
```

represents:
```text
files and directories
```

in the system.

---

# File Operations Used

| Method | Purpose |
|---|---|
| exists() | Check existence |
| isDirectory() | Check directory |
| isFile() | Check file |
| listFiles() | List contents |
| getName() | Get file name |
| getAbsolutePath() | Full file path |

---

# Recursive Function

A recursive function:
```text
calls itself repeatedly
```

until condition satisfied.

Used here for:
```text
traversing subdirectories
```

---

# Directory Traversal

Program recursively explores:
- folders
- subfolders
- files

---

# listFilesAndDirectories()

This method:
```text
lists all files and directories
```

inside specified folder.

---

# searchFile()

This method:
```text
searches file recursively
```

inside:
- directory
- subdirectories

---

# Absolute Path

```java
getAbsolutePath()
```

returns:
```text
full location of file
```

Example:

```text
C:\Users\Akhil\Documents\file.txt
```

---

# Boolean Variable found

```java
static boolean found=false;
```

tracks:
```text
whether file found or not
```

---

# Detailed Algorithm

1. Import:
```java
java.io.File
```

2. Create class:
```java
P25_DirectoryListing
```

3. Create:
```java
listFilesAndDirectories()
```

method.

4. Get file list using:
```java
listFiles()
```

5. Display file names.

6. If directory found:
   - recursively call method

7. Create:
```java
searchFile()
```

method.

8. Compare file names.

9. If match found:
   - display absolute path

10. If subdirectory found:
   - recursively search

11. In main method:
   - read directory path

12. Create:
```java
File
```

object.

13. Check:
- exists()
- isDirectory()

14. Display directory contents.

15. Read file name.

16. Search file recursively.

17. Display result.

18. Close scanner.

19. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Directory Path
   ↓
Check Directory Validity
   ↓
List Files and Directories
   ↓
Read File Name
   ↓
Search File Recursively
   ↓
Display Result
   ↓
Stop
```

---

# Sample Input

```text
Enter the directory path:
C:\JavaPrograms

Enter the file name to search:
sample.txt
```

---

# Sample Output

```text
Files and directories in the specified directory:

Programs
Notes
sample.txt

Searching for file 'sample.txt'...

File found at:
C:\JavaPrograms\sample.txt
```

---

# Dry Run

Directory:
```text
Documents
```

Contents:
```text
Projects
Notes.txt
Java
```

Program:
- lists contents
- enters subfolders recursively
- searches target file

---

# Internal Working

Program recursively traverses:
```text
directory tree
```

Each folder:
```text
searched separately
```

---

# Recursive Traversal Example

```text
Root
 ├── Folder1
 │    ├── File1
 │    └── File2
 └── Folder2
      └── File3
```

Program visits:
```text
all folders recursively
```

---

# Time Complexity

Directory traversal:

:contentReference[oaicite:0]{index=0}

where:
```text
n = total files and directories
```

---

# Space Complexity

Recursive stack:

:contentReference[oaicite:1]{index=1}

where:
```text
h = directory depth
```

---

# Advantages

- Recursive directory traversal
- Automatic file searching
- Displays complete file structure
- Uses built-in Java file handling

---

# Limitations

- Case-sensitive search
- Large directories may take time
- Recursive depth may become large

---

# Edge Cases

## Case 1: Invalid Directory

Displays:
```text
Invalid directory path
```

---

## Case 2: Empty Directory

Nothing displayed.

---

## Case 3: File Not Found

Displays:
```text
File not found
```

---

# Possible Improvements

- Case-insensitive search
- Search by extension
- GUI based file explorer
- Display directory hierarchy

---

# Possible Errors

## 1. SecurityException

Occurs if permission denied.

---

## 2. NullPointerException

Possible if:
```java
listFiles()
```

returns null.

---

# Viva Questions

## Q1. Which package used for file handling?

```java
java.io
```

---

## Q2. Which class represents files and directories?

```java
File
```

---

## Q3. Which method lists directory contents?

```java
listFiles()
```

---

## Q4. Which method checks file existence?

```java
exists()
```

---

## Q5. Which method checks directory?

```java
isDirectory()
```

---

## Q6. What is recursion?
Function calling itself.

---

## Q7. Which method returns absolute path?

```java
getAbsolutePath()
```

---

## Q8. Time complexity of traversal?

:contentReference[oaicite:2]{index=2}

---

## Q9. Space complexity?

:contentReference[oaicite:3]{index=3}

---

## Q10. What happens if directory invalid?
Program prints invalid directory message.