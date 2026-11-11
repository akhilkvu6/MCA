# Program 27 - Copy File to Another File

## Question

Write a program to copy the contents of one file into another file.

---

# Filename

```text
P27_FileCopy.java
```

---

# Source Code

```java
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
```

---

# Concepts Used

- File Handling
- FileReader
- FileWriter
- Character Stream
- Reading Files
- Writing Files
- Exception Handling
- IOException

---

# Theory

Java provides:
```java
java.io
```

package for:
```text
input and output operations
```

This program demonstrates:
- reading contents from one file
- writing contents into another file

---

# FileReader

```java
FileReader
```

used for:
```text
reading character data from file
```

---

# FileWriter

```java
FileWriter
```

used for:
```text
writing character data into file
```

---

# Character Stream

Character stream handles:
```text
text data character by character
```

Used mainly for:
- text files
- source code files
- documents

---

# read() Method

```java
f1.read()
```

reads:
```text
one character at a time
```

Returns:
```text
ASCII/Unicode value
```

---

# write() Method

```java
f2.write(ch)
```

writes:
```text
character into destination file
```

---

# EOF Condition

```java
-1
```

indicates:
```text
end of file
```

---

# IOException

```java
IOException
```

handles:
```text
file related errors
```

Examples:
- file missing
- invalid path
- permission denied

---

# Detailed Algorithm

1. Import:
```java
java.io.*
```

2. Import:
```java
Scanner
```

3. Create class:
```java
P27_FileCopy
```

4. Start:
```java
try
```

block.

5. Create:
```java
Scanner
```

object.

6. Read:
- source file path
- destination file path

7. Create:
```java
FileReader
```

for source file.

8. Create:
```java
FileWriter
```

for destination file.

9. Read source file:
```text
character by character
```

10. Write characters into destination file.

11. Continue until:
```text
end of file
```

12. Close:
- FileReader
- FileWriter
- Scanner

13. Display:
```text
File copied successfully
```

14. Catch:
```java
IOException
```

15. Display error message.

16. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Source File Path
   ↓
Read Destination File Path
   ↓
Open Source File
   ↓
Open Destination File
   ↓
Read Character
   ↓
Write Character
   ↓
Repeat Until EOF
   ↓
Close Files
   ↓
Display Success Message
   ↓
Stop
```

---

# Sample Input

```text
Enter the source file path:
file1.txt

Enter the destination file path:
file2.txt
```

---

# Sample Output

```text
File copied successfully.
```

---

# Example

## Source File

```text
Hello Java
```

---

## Destination File After Copy

```text
Hello Java
```

---

# Dry Run

Source file:
```text
ABC
```

Program reads:
```text
A
```

writes:
```text
A
```

Reads:
```text
B
```

writes:
```text
B
```

Reads:
```text
C
```

writes:
```text
C
```

EOF reached.

---

# Internal Working

Program:
```text
opens source file
```

Then:
```text
reads each character
```

Each character copied into:
```text
destination file
```

---

# File Handling Process

```text
Source File
     ↓
FileReader
     ↓
Character Read
     ↓
FileWriter
     ↓
Destination File
```

---

# Time Complexity

Reading and writing:

:contentReference[oaicite:0]{index=0}

where:
```text
n = number of characters
```

---

# Space Complexity

:contentReference[oaicite:1]{index=1}

---

# Advantages

- Simple implementation
- Works for text files
- Uses character streams
- Automatic destination file creation

---

# Limitations

- Suitable mainly for text files
- Slower for large files
- Reads one character at a time

---

# Edge Cases

## Case 1: Source File Missing

Throws:
```text
FileNotFoundException
```

---

## Case 2: Empty Source File

Destination file becomes empty.

---

## Case 3: Invalid Path

IOException occurs.

---

# Possible Improvements

- Use BufferedReader and BufferedWriter
- Copy binary files using byte streams
- Add append mode
- Display file size

---

# Possible Errors

## 1. FileNotFoundException

Occurs if source file missing.

---

## 2. IOException

Occurs during file operations.

---

# Viva Questions

## Q1. Which package used for file handling?

```java
java.io
```

---

## Q2. Which class reads character data?

```java
FileReader
```

---

## Q3. Which class writes character data?

```java
FileWriter
```

---

## Q4. What does read() return?
Character value from file.

---

## Q5. What indicates end of file?

```text
-1
```

---

## Q6. Why close files?
To release system resources.

---

## Q7. Which stream used for text files?
Character stream.

---

## Q8. Which stream used for binary files?
Byte stream.

---

## Q9. Time complexity of file copy?

:contentReference[oaicite:2]{index=2}

---

## Q10. Difference between FileReader and FileInputStream?

| FileReader | FileInputStream |
|---|---|
| Character stream | Byte stream |
| Text files | Binary files |