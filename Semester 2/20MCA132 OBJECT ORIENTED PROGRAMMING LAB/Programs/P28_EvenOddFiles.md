# Program 28 - Even and Odd Numbers into Separate Files

## Question

Write a program that reads integers from a file and copies even numbers and odd numbers into separate files.

---

# Filename

```text
P28_EvenOddFiles.java
```

---

# Source Code

```java
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
```

---

# Concepts Used

- File Handling
- FileReader
- FileWriter
- Scanner Class
- Integer Processing
- Even and Odd Numbers
- Exception Handling
- IOException

---

# Theory

This program:
```text
reads integers from a file
```

and separates them into:
- even numbers
- odd numbers

stored in:
- even.txt
- odd.txt

---

# File Handling

Java uses:
```java
java.io
```

package for:
```text
file operations
```

---

# Scanner Class

```java
Scanner
```

used for:
```text
reading integers from file
```

---

# FileWriter

```java
FileWriter
```

used for:
```text
writing text into files
```

---

# Even Number

A number divisible by:
```text
2
```

is:
```text
even
```

Condition:

:contentReference[oaicite:0]{index=0}

---

# Odd Number

A number not divisible by:
```text
2
```

is:
```text
odd
```

Condition:

:contentReference[oaicite:1]{index=1}

---

# hasNextInt()

```java
hasNextInt()
```

checks:
```text
whether next integer exists
```

---

# write() Method

```java
write()
```

writes:
```text
data into file
```

---

# Detailed Algorithm

1. Import:
```java
java.io.*
```

2. Import:
```java
java.util.*
```

3. Create class:
```java
P28_EvenOddFiles
```

4. Start:
```java
try
```

block.

5. Read source file name.

6. Create:
```java
Scanner
```

for source file.

7. Create:
- even.txt
- odd.txt

using:
```java
FileWriter
```

8. Read integers from source file.

9. Check:
```java
num % 2 == 0
```

10. If even:
   - write into even.txt

11. Else:
   - write into odd.txt

12. Continue until file ends.

13. Close:
- FileWriter
- Scanner

14. Display success messages.

15. Catch:
```java
IOException
```

16. Display error message.

17. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Source File
   ↓
Open even.txt
   ↓
Open odd.txt
   ↓
Read Integer
   ↓
Check Even or Odd
   ↓
Write to Corresponding File
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

# Sample Input File

## numbers.txt

```text
10 15 20 25 30 35 40
```

---

# Sample Output

```text
Even numbers copied to even.txt

Odd numbers copied to odd.txt
```

---

# even.txt

```text
10 20 30 40
```

---

# odd.txt

```text
15 25 35
```

---

# Dry Run

Input:
```text
10
```

Check:

:contentReference[oaicite:2]{index=2}

Even.

Stored in:
```text
even.txt
```

---

Input:
```text
15
```

Check:

:contentReference[oaicite:3]{index=3}

Odd.

Stored in:
```text
odd.txt
```

---

# Internal Working

Program:
```text
reads integers one by one
```

Then:
```text
checks divisibility by 2
```

Numbers written into:
- even file
- odd file

---

# Files Created

| File | Contents |
|---|---|
| even.txt | Even numbers |
| odd.txt | Odd numbers |

---

# Time Complexity

Reading and classification:

:contentReference[oaicite:4]{index=4}

where:
```text
n = number of integers
```

---

# Space Complexity

:contentReference[oaicite:5]{index=5}

---

# Advantages

- Simple file processing
- Separates numbers efficiently
- Automatic file creation
- Easy implementation

---

# Limitations

- Handles integers only
- Invalid file data may cause issues
- No buffering used

---

# Edge Cases

## Case 1: Empty File

No output numbers written.

---

## Case 2: Invalid File Name

IOException occurs.

---

## Case 3: Non-integer Data

Scanner stops reading integers.

---

# Possible Improvements

- Use BufferedWriter
- Handle negative numbers separately
- Display file contents after copying

---

# Possible Errors

## 1. FileNotFoundException

Occurs if source file missing.

---

## 2. IOException

Occurs during file operations.

---

## 3. InputMismatchException

Occurs for invalid data type.

---

# Viva Questions

## Q1. Which package used for file handling?

```java
java.io
```

---

## Q2. Which class reads data from file?

```java
Scanner
```

---

## Q3. Which class writes data into file?

```java
FileWriter
```

---

## Q4. Condition for even number?

:contentReference[oaicite:6]{index=6}

---

## Q5. Condition for odd number?

:contentReference[oaicite:7]{index=7}

---

## Q6. Which method checks next integer?

```java
hasNextInt()
```

---

## Q7. Which files created in program?

```text
even.txt
odd.txt
```

---

## Q8. Time complexity?

:contentReference[oaicite:8]{index=8}

---

## Q9. Space complexity?

:contentReference[oaicite:9]{index=9}

---

## Q10. What happens if file missing?
Program throws exception.