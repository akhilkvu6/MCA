# Program 15 - User Defined Exception

## Question

Write a user defined exception class to authenticate the username and password.

---

# Filename

```text
P15_UserDefinedException.java
```

---

# Source Code

```java
import java.util.*;

class nameexception extends RuntimeException
{
    nameexception(String s)
    {
        super(s);
    }
}

class passexception extends RuntimeException
{
    passexception(String s)
    {
        super(s);
    }
}

class user
{
    String name,password;

    user(String n,String p)
    {
        name=n;
        password=p;
    }

    void login(String n,String p)
    {
        try
        {
            if(name.equals(n)&&password.equals(p))
            {
                System.out.println("\t\tLogin successful");
            }

            else
            {
                throw new passexception("Invalid username or password!!");
            }
        }

        catch(passexception e)
        {
            System.out.println("\n"+e.getMessage());
            System.exit(0);
        }
    }
}

public class P15_UserDefinedException
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        System.out.print("Enter name: ");
        String s=sc.next();

        try
        {
            for(int i=0;i<s.length();i++)
            {
                char ch=s.charAt(i);

                if((ch>=65&&ch<=90)||(ch>=97&&ch<=122))
                {
                    continue;
                }

                else
                {
                    throw new nameexception("Invalid Name");
                }
            }
        }

        catch(nameexception e)
        {
            System.out.println("\n"+e.getMessage());
            System.exit(0);
        }

        System.out.print("Enter password: ");
        String pass=sc.next();

        try
        {
            int p=0;

            if(pass.length()<8)
            {
                throw new nameexception("Password must have 8 characters");
            }

            for(int i=0;i<pass.length();i++)
            {
                char ch=pass.charAt(i);

                if((ch>=48&&ch<=57))
                {
                    p=1;
                }
            }

            if(p==0)
            {
                throw new passexception("Password must contain atleast 1 number");
            }
        }

        catch(nameexception e)
        {
            System.out.println("\n"+e.getMessage());
            System.exit(0);
        }

        catch(passexception e)
        {
            System.out.println("\n"+e.getMessage());
            System.exit(0);
        }

        user u1=new user(s,pass);

        System.out.println("\t\tLogin!!");

        System.out.print("Username: ");
        String n1=sc.next();

        System.out.print("Password: ");
        String p1=sc.next();

        u1.login(n1,p1);
    }
}
```

---

# Concepts Used

- Exception Handling
- User Defined Exception
- RuntimeException
- try-catch
- throw Keyword
- String Validation
- Password Validation
- Scanner Class
- Object Oriented Programming

---

# Theory

Exception handling is used to:
```text
handle runtime errors
```

Java allows creation of:
```text
custom exceptions
```

called:
```text
User Defined Exceptions
```

---

# User Defined Exception

Custom exception classes are created by:
```text
extending Exception or RuntimeException
```

In this program:
- nameexception
- passexception

are custom exceptions.

---

# RuntimeException

```java
class nameexception extends RuntimeException
```

RuntimeException is:
```text
unchecked exception
```

Compiler does not force handling.

---

# Purpose of Program

This program validates:
- username
- password

using:
```text
custom exception handling
```

---

# Username Validation

Checks whether:
```text
all characters are alphabets
```

If invalid:
```java
throw new nameexception("Invalid Name");
```

---

# Password Validation

Checks:
- minimum 8 characters
- contains at least one digit

---

# Login Authentication

Compares:
- stored username/password
with
- entered login credentials

---

# throw Keyword

```java
throw new passexception(...)
```

Used to:
```text
manually generate exception
```

---

# try-catch Block

Used to:
```text
detect and handle exceptions
```

---

# Detailed Algorithm

1. Create class:
```java
nameexception
```

2. Extend:
```java
RuntimeException
```

3. Create class:
```java
passexception
```

4. Extend:
```java
RuntimeException
```

5. Create class:
```java
user
```

6. Declare:
- name
- password

7. Create constructor.

8. Create:
```java
login()
```

method.

9. Compare username and password.

10. Throw exception if invalid.

11. In main method:
   - read username

12. Validate each character.

13. If non-alphabet found:
```java
throw new nameexception
```

14. Read password.

15. Check password length.

16. Check presence of digit.

17. Throw exceptions if invalid.

18. Create user object.

19. Read login credentials.

20. Call:
```java
login()
```

21. Display result.

22. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Username
   ↓
Validate Username
   ↓
Read Password
   ↓
Validate Password
   ↓
Create User Object
   ↓
Login Authentication
   ↓
Valid?
   ↓
Display Result
   ↓
Stop
```

---

# Sample Input

```text
Enter name: Akhil

Enter password: akhil123

Login!!

Username: Akhil

Password: akhil123
```

---

# Sample Output

```text
Login successful
```

---

# Invalid Username Example

Input:

```text
Akhil123
```

Output:

```text
Invalid Name
```

---

# Invalid Password Example

Input:

```text
akhil
```

Output:

```text
Password must have 8 characters
```

---

# Dry Run

Username:
```text
Akhil
```

Each character checked:
```text
A → valid
k → valid
h → valid
i → valid
l → valid
```

---

# Password:
```text
akhil123
```

Checks:
- length ≥ 8
- contains digit

Both valid.

---

# Internal Working

Program validates:
```text
input step-by-step
```

Custom exceptions provide:
```text
specific error messages
```

---

# ASCII Values Used

## Alphabets

| Character | ASCII Range |
|---|---|
| A-Z | 65-90 |
| a-z | 97-122 |

---

# Digits

| Character | ASCII Range |
|---|---|
| 0-9 | 48-57 |

---

# Time Complexity

Username validation:

:contentReference[oaicite:0]{index=0}

Password validation:

:contentReference[oaicite:1]{index=1}

where:
```text
n = string length
```

---

# Space Complexity

:contentReference[oaicite:2]{index=2}

---

# Advantages

- Custom error handling
- Better validation
- Improved readability
- Reusable exception classes

---

# Limitations

- ASCII checking is lengthy
- Does not encrypt password

---

# Edge Cases

## Case 1: Empty Username

Validation fails.

---

## Case 2: Password Without Number

Exception thrown.

---

## Case 3: Password Length < 8

Exception thrown.

---

# Possible Improvements

- Use regex validation
- Encrypt password
- Hide password input
- Add special character validation

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. Custom Exceptions

- Invalid Name
- Invalid Password

---

# Viva Questions

## Q1. What is exception handling?
Mechanism to handle runtime errors.

---

## Q2. What is user defined exception?
Custom exception created by programmer.

---

## Q3. Which keyword is used to throw exception?

```java
throw
```

---

## Q4. Which class is extended here?

```java
RuntimeException
```

---

## Q5. Difference between checked and unchecked exception?

| Checked | Unchecked |
|---|---|
| Checked at compile time | Checked at runtime |

---

## Q6. What is try block?
Contains risky code.

---

## Q7. What is catch block?
Handles exception.

---

## Q8. What is RuntimeException?
Unchecked exception class.

---

## Q9. Why validate password?
Improve security.

---

## Q10. What is time complexity?

:contentReference[oaicite:3]{index=3}