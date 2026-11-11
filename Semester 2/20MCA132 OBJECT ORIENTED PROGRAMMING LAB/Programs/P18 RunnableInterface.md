# Program 18 - Runnable Interface

## Question

Define 2 classes:
- one for generating Fibonacci numbers
- another for displaying even numbers in a given range

Implement using threads with Runnable Interface.

---

# Filename

```text
P18_RunnableInterface.java
```

---

# Source Code

```java
import java.util.*;

class fibonacci implements Runnable
{
    int n;

    fibonacci(int limit)
    {
        n=limit;
    }

    public void run()
    {
        int a=0,b=1,c;

        for(int i=1;i<=n;i++)
        {
            System.out.println("Fibonacci: "+a);

            c=a+b;
            a=b;
            b=c;
        }
    }
}

class Even implements Runnable
{
    int start,end;

    Even(int a,int b)
    {
        start=a;
        end=b;
    }

    public void run()
    {
        for(int i=start;i<=end;i++)
        {
            if(i%2==0)
            {
                System.out.println("Even: "+i);
            }
        }
    }
}

public class P18_RunnableInterface
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        System.out.print("Enter the number of Fibonacci numbers: ");
        int n=sc.nextInt();

        System.out.print("Enter the start and end range for even numbers: ");
        int start=sc.nextInt();
        int end=sc.nextInt();

        Thread f=new Thread(new fibonacci(n));
        Thread e=new Thread(new Even(start,end));

        f.start();
        e.start();
    }
}
```

---

# Concepts Used

- Multithreading
- Runnable Interface
- Thread Class
- Fibonacci Series
- Even Number Generation
- Parallel Execution
- Scanner Class
- Object Oriented Programming

---

# Theory

A thread is:
```text
lightweight subprocess
```

Threads allow:
```text
multiple tasks to execute simultaneously
```

This program demonstrates:
```text
multithreading using Runnable interface
```

---

# Runnable Interface

```java
Runnable
```

is an interface used for:
```text
creating threads
```

Classes implement:
```java
run()
```

method.

---

# Difference Between Thread Class and Runnable Interface

| Thread Class | Runnable Interface |
|---|---|
| Class extends Thread | Class implements Runnable |
| Single inheritance limitation | Better flexibility |
| Direct thread object | Thread object created separately |

---

# Fibonacci Series

Fibonacci series:

```text
0 1 1 2 3 5 8 ...
```

Each term:

:contentReference[oaicite:0]{index=0}

---

# Even Numbers

Even number:

:contentReference[oaicite:1]{index=1}

---

# fibonacci Class

Implements:
```java
Runnable
```

Generates:
```text
Fibonacci series
```

---

# Even Class

Implements:
```java
Runnable
```

Generates:
```text
even numbers in range
```

---

# Thread Object Creation

```java
Thread f=new Thread(new fibonacci(n));
```

Creates thread using:
```text
Runnable object
```

---

# start() Method

```java
start()
```

starts:
```text
thread execution
```

---

# Detailed Algorithm

1. Create class:
```java
fibonacci
```

2. Implement:
```java
Runnable
```

3. Declare:
```java
n
```

4. Create constructor.

5. Override:
```java
run()
```

6. Generate Fibonacci series.

7. Create class:
```java
Even
```

8. Implement:
```java
Runnable
```

9. Declare:
```java
start
```

and:
```java
end
```

10. Override:
```java
run()
```

11. Check:
```java
i % 2 == 0
```

12. Print even numbers.

13. In main method:
   - read inputs

14. Create thread objects.

15. Start threads using:
```java
start()
```

16. Execute concurrently.

17. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Fibonacci Limit
   ↓
Read Even Number Range
   ↓
Create Runnable Objects
   ↓
Create Thread Objects
   ↓
Start Threads
   ↓
Generate Fibonacci Numbers
   ↓
Generate Even Numbers
   ↓
Display Results
   ↓
Stop
```

---

# Sample Input

```text
Enter the number of Fibonacci numbers: 7

Enter the start and end range for even numbers: 1 10
```

---

# Sample Output

```text
Fibonacci: 0
Fibonacci: 1
Fibonacci: 1
Fibonacci: 2
Fibonacci: 3
Fibonacci: 5
Fibonacci: 8

Even: 2
Even: 4
Even: 6
Even: 8
Even: 10
```

---

# Dry Run

Fibonacci:

```text
a=0
b=1
```

Iteration 1:
```text
print 0
c=1
```

Iteration 2:
```text
print 1
c=2
```

---

Even numbers:

Range:
```text
1 to 10
```

Checks:
```text
2 % 2 = 0
4 % 2 = 0
```

Even numbers printed.

---

# Internal Working

Program creates:
```text
two separate threads
```

One thread:
```text
generates Fibonacci numbers
```

Another thread:
```text
generates even numbers
```

Both execute:
```text
simultaneously
```

---

# Time Complexity

Fibonacci generation:

:contentReference[oaicite:2]{index=2}

---

Even number generation:

:contentReference[oaicite:3]{index=3}

---

# Space Complexity

:contentReference[oaicite:4]{index=4}

---

# Advantages

- Better flexibility than Thread class
- Supports multithreading
- Efficient execution
- Allows multiple inheritance

---

# Limitations

- Output order may vary
- No synchronization

---

# Edge Cases

## Case 1: n = 0

No Fibonacci numbers generated.

---

## Case 2: Negative Range

Even loop may not execute.

---

## Case 3: start > end

No even numbers printed.

---

# Possible Improvements

- Add synchronization
- Optimize Fibonacci using recursion
- Use lambda expressions

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. Logical Errors

Wrong loop condition may cause incorrect output.

---

# Viva Questions

## Q1. What is Runnable interface?
Interface used to create threads.

---

## Q2. Which method must Runnable implement?

```java
run()
```

---

## Q3. Which method starts thread?

```java
start()
```

---

## Q4. Difference between Thread and Runnable?

Runnable supports better flexibility.

---

## Q5. What is multithreading?
Executing multiple threads simultaneously.

---

## Q6. What is Fibonacci series?

:contentReference[oaicite:5]{index=5}

---

## Q7. Condition for even number?

:contentReference[oaicite:6]{index=6}

---

## Q8. What is concurrency?
Multiple tasks executing together.

---

## Q9. What is time complexity of Fibonacci generation?

:contentReference[oaicite:7]{index=7}

---

## Q10. What is space complexity?

:contentReference[oaicite:8]{index=8}