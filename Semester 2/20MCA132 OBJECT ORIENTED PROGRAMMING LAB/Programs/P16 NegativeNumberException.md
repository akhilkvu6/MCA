# Program 16 - User Defined Exception (Negative Numbers)

## Question

Find the average of N positive integers, raising a user defined exception for each negative input.

---

# Filename

```text
P16_NegativeNumberException.java
```

---

# Source Code

```java
import java.util.*;

class negative extends RuntimeException
{
    negative(String s)
    {
        super(s);
    }
}

public class P16_NegativeNumberException
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        System.out.print("Enter no:of elements: ");

        int n=sc.nextInt();

        int nos[]=new int[n];

        double sum=0;

        System.out.print("Enter "+n+" numbers: ");

        for(int i=0;i<n;i++)
        {
            nos[i]=sc.nextInt();

            try
            {
                if(nos[i]<0)
                {
                    throw new negative("Negative number is not allowed!!!");
                }

                else
                {
                    sum+=nos[i];
                }
            }

            catch(negative e)
            {
                System.out.println("\n"+e.getMessage());

                System.exit(0);
            }
        }

        System.out.println("Average: "+String.format("%.2f",sum/n));
    }
}
```

---

# Concepts Used

- User Defined Exception
- RuntimeException
- Exception Handling
- Arrays
- Looping
- Conditional Statements
- Scanner Class
- Average Calculation

---

# Theory

Exception handling is used to:
```text
handle runtime errors
```

This program demonstrates:
```text
user defined exception handling
```

for:
```text
negative numbers
```

---

# User Defined Exception

Custom exception class:

```java
class negative extends RuntimeException
```

is created to:
```text
handle invalid negative input
```

---

# RuntimeException

```java
RuntimeException
```

is:
```text
unchecked exception
```

It occurs during:
```text
runtime
```

---

# Purpose of Program

Program:
- reads positive integers
- checks for negative values
- calculates average

If negative number entered:
```text
custom exception is raised
```

---

# Array Used

```java
int nos[]
```

stores:
```text
input numbers
```

---

# Average Formula

:contentReference[oaicite:0]{index=0}

---

# throw Keyword

```java
throw new negative(...)
```

Used to:
```text
manually generate exception
```

---

# try-catch Block

Used to:
- detect exceptions
- handle exceptions

---

# Detailed Algorithm

1. Create class:
```java
negative
```

2. Extend:
```java
RuntimeException
```

3. Create main class:
```java
P16_NegativeNumberException
```

4. Read:
```java
n
```

(number of elements)

5. Create array:
```java
nos[]
```

6. Initialize:
```java
sum = 0
```

7. Read array elements.

8. Check:
```java
nos[i] < 0
```

9. If true:
```java
throw new negative(...)
```

10. Else:
```java
sum += nos[i]
```

11. Catch exception.

12. Display error message.

13. Calculate average.

14. Display result.

15. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Number of Elements
   ↓
Read Array Elements
   ↓
Check Negative?
   ↓
Yes → Throw Exception
   ↓
No → Add to Sum
   ↓
Calculate Average
   ↓
Display Result
   ↓
Stop
```

---

# Sample Input

```text
Enter no:of elements: 5

Enter 5 numbers:
10
20
30
40
50
```

---

# Sample Output

```text
Average: 30.00
```

---

# Negative Input Example

Input:

```text
10
20
-5
30
```

Output:

```text
Negative number is not allowed!!!
```

---

# Dry Run

Input:
```text
10 20 30
```

Sum calculation:

```text
sum = 10
sum = 30
sum = 60
```

Average:

:contentReference[oaicite:1]{index=1}

---

# Internal Working

Program validates:
```text
every number individually
```

If negative:
```text
custom exception interrupts execution
```

Else:
```text
sum is updated
```

---

# Time Complexity

Array traversal:

:contentReference[oaicite:2]{index=2}

where:
```text
n = number of elements
```

---

# Space Complexity

Array storage:

:contentReference[oaicite:3]{index=3}

---

# Advantages

- Prevents invalid input
- Demonstrates custom exceptions
- Simple implementation
- Easy validation

---

# Limitations

- Program terminates immediately after exception
- Does not allow re-entry of values

---

# Edge Cases

## Case 1: Negative Number

Exception raised.

---

## Case 2: Zero

Accepted as valid input.

---

## Case 3: Large Numbers

Handled normally if within integer range.

---

# Possible Improvements

- Allow re-entering invalid number
- Use Exception instead of RuntimeException
- Validate decimal numbers

---

# Possible Errors

## 1. InputMismatchException

Occurs when non-integer entered.

---

## 2. Custom Exception

Occurs for negative numbers.

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

## Q5. What is RuntimeException?
Unchecked exception class.

---

## Q6. Why use custom exception?
To handle specific errors.

---

## Q7. What is average formula?

:contentReference[oaicite:4]{index=4}

---

## Q8. Which loop is used?
for loop.

---

## Q9. What is time complexity?

:contentReference[oaicite:5]{index=5}

---

## Q10. What happens when negative number entered?
Program throws custom exception.