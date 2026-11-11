# Program 26 - Files Write and Read

## Question

Write a program to write to a file, then read from the file and display the contents on the console.

---

# Filename

```text
P26_WriteRead.java
```

---

# Source Code

```java
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
```

---

# Concepts Used

- File Handling
- FileInputStream
- FileOutputStream
- Byte Stream
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
- writing data into file
- reading data from file

---

# FileOutputStream

```java
FileOutputStream
```

used for:
```text
writing bytes into file
```

---

# FileInputStream

```java
FileInputStream
```

used for:
```text
reading bytes from file
```

---

# Byte Stream

Byte stream handles:
```text
binary data and text data
```

Data is processed:
```text
byte by byte
```

---

# getBytes() Method

```java
data.getBytes()
```

converts:
```text
string into byte array
```

---

# write() Method

```java
fout.write(b)
```

writes:
```text
byte array into file
```

---

# read() Method

```java
fin.read()
```

reads:
```text
one byte at a time
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
- permission denied
- invalid file path

---

# Detailed Algorithm

1. Import:
```java
java.io.*
```

2. Create class:
```java
P26_WriteRead
```

3. Start:
```java
try
```

block.

4. Create:
```java
FileOutputStream
```

object.

5. Store text in string variable.

6. Convert string into bytes.

7. Write bytes into file.

8. Close output stream.

9. Create:
```java
FileInputStream
```

object.

10. Read file byte by byte.

11. Convert byte into character.

12. Display contents.

13. Close input stream.

14. Catch:
```java
IOException
```

15. Display exception if error occurs.

16. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create FileOutputStream
   ↓
Convert String to Bytes
   ↓
Write Data to File
   ↓
Close Output Stream
   ↓
Create FileInputStream
   ↓
Read File Byte by Byte
   ↓
Display File Contents
   ↓
Close Input Stream
   ↓
Stop
```

---

# Sample Output

```text
This is the implementation of write and read operation
```

---

# Dry Run

String:
```text
Hello
```

Converted to bytes:
```text
72 101 108 108 111
```

Written into file.

Program reads:
```text
72 → H
101 → e
```

and displays:
```text
Hello
```

---

# Internal Working

Program creates:
```text
data.txt
```

Text stored:
```text
as bytes
```

Program reads:
```text
one byte at a time
```

and converts into:
```text
characters
```

---

# File Created

```text
data.txt
```

Contents:
```text
This is the implementation of write and read operation
```

---

# Time Complexity

Writing operation:

:contentReference[oaicite:0]{index=0}

---

Reading operation:

:contentReference[oaicite:1]{index=1}

where:
```text
n = number of characters
```

---

# Space Complexity

:contentReference[oaicite:2]{index=2}

---

# Advantages

- Simple file handling
- Efficient byte stream operations
- Supports binary files
- Easy implementation

---

# Limitations

- Reads one byte at a time
- Not efficient for large files
- No buffering

---

# Edge Cases

## Case 1: File Not Found

Throws:
```text
FileNotFoundException
```

---

## Case 2: Empty File

Nothing displayed.

---

## Case 3: Permission Denied

IOException occurs.

---

# Possible Improvements

- Use BufferedInputStream
- Read user input dynamically
- Use FileReader and FileWriter for text files

---

# Possible Errors

## 1. IOException

Occurs during file operations.

---

## 2. FileNotFoundException

Occurs if file missing or invalid path.

---

# Viva Questions

## Q1. Which package used for file handling?

```java
java.io
```

---

## Q2. Which class writes bytes into file?

```java
FileOutputStream
```

---

## Q3. Which class reads bytes from file?

```java
FileInputStream
```

---

## Q4. What does getBytes() do?
Converts string into byte array.

---

## Q5. What does read() return?
Next byte from file.

---

## Q6. What indicates end of file?

```text
-1
```

---

## Q7. Why close streams?
To release system resources.

---

## Q8. What is IOException?
Exception for file handling errors.

---

## Q9. Time complexity of reading?

:contentReference[oaicite:3]{index=3}

---

## Q10. Difference between byte stream and character stream?

| Byte Stream | Character Stream |
|---|---|
| Handles bytes | Handles characters |