# Program 17 - Thread Class

## Question

Define 2 classes:
- one for generating multiplication table of 5
- another for displaying first N prime numbers

Implement using thread class.

---

# Filename

```text
P17_ThreadClass.java
```

---

# Source Code

```java
import java.util.*;

class multiple5 extends Thread
{
    public void run()
    {
        for(int i=1;i<=10;i++)
        {
            System.out.println(i+" x 5 = "+(i*5));
        }
    }
}

class Prime extends Thread
{
    int n;

    Prime(int limit)
    {
        n=limit;
    }

    int isprime(int n)
    {
        if(n<2)
        {
            return 0;
        }

        for(int i=2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                return 0;
            }
        }

        return 1;
    }

    public void run()
    {
        for(int i=1;i<=n;i++)
        {
            if(isprime(i)==1)
            {
                System.out.println("Prime: "+i);
            }
        }
    }
}

public class P17_ThreadClass
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        multiple5 m=new multiple5();

        System.out.print("Enter limit for generating prime: ");

        int n=sc.nextInt();

        Prime m1=new Prime(n);

        m.start();

        m1.start();
    }
}
```

---

# Concepts Used

- Multithreading
- Thread Class
- Inheritance
- Method Overriding
- Prime Number Logic
- Loops
- Scanner Class
- Parallel Execution

---

# Theory

A thread is:
```text
a lightweight sub-process
```

Threads allow:
```text
multiple tasks to run simultaneously
```

This program demonstrates:
- thread creation
- concurrent execution

---

# Thread Class

Java provides:
```java
Thread
```

class for:
```text
multithreading
```

A class becomes thread by:
```text
extending Thread class
```

---

# run() Method

```java
public void run()
```

contains:
```text
task executed by thread
```

---

# start() Method

```java
start()
```

creates:
```text
new thread execution
```

Internally:
```text
calls run()
```

---

# multiple5 Class

Generates:
```text
multiplication table of 5
```

---

# Prime Class

Generates:
```text
prime numbers
```

upto:
```text
n
```

---

# Prime Number

A prime number:
```text
has exactly 2 factors
```

Examples:
```text
2 3 5 7 11
```

---

# Prime Checking Logic

```java
isprime(int n)
```

Checks divisibility from:
```text
2 to n/2
```

If divisible:
```text
not prime
```

Else:
```text
prime
```

---

# Detailed Algorithm

1. Create class:
```java
multiple5
```

2. Extend:
```java
Thread
```

3. Override:
```java
run()
```

4. Print multiplication table of 5.

5. Create class:
```java
Prime
```

6. Extend:
```java
Thread
```

7. Declare:
```java
n
```

8. Create constructor.

9. Define:
```java
isprime()
```

method.

10. Check prime logic.

11. Override:
```java
run()
```

12. Generate prime numbers.

13. In main method:
   - create thread objects

14. Read limit.

15. Start threads using:
```java
start()
```

16. Threads execute simultaneously.

17. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create Thread Objects
   ↓
Read Limit
   ↓
Start Thread 1
   ↓
Generate Table of 5
   ↓
Start Thread 2
   ↓
Generate Prime Numbers
   ↓
Display Results
   ↓
Stop
```

---

# Sample Input

```text
Enter limit for generating prime: 10
```

---

# Sample Output

```text
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

Prime: 2
Prime: 3
Prime: 5
Prime: 7
```

---

# Dry Run

Input:
```text
10
```

Thread 1:
```text
prints multiplication table
```

Thread 2:
```text
checks prime numbers
```

Prime check example:

For:
```text
5
```

Check:
```text
5 % 2 ≠ 0
```

No divisors found.

Result:
```text
Prime
```

---

# Internal Working

Program creates:
```text
two independent threads
```

Both execute:
```text
concurrently
```

CPU switches between threads during execution.

---

# Time Complexity

Multiplication thread:

:contentReference[oaicite:0]{index=0}

---

Prime generation:

:contentReference[oaicite:1]{index=1}

because:
```text
nested iterations used
```

---

# Space Complexity

:contentReference[oaicite:2]{index=2}

---

# Advantages

- Parallel execution
- Faster task handling
- Better CPU utilization
- Demonstrates multithreading

---

# Limitations

- Output order may vary
- Prime checking not optimized

---

# Edge Cases

## Case 1: n = 1

No prime numbers generated.

---

## Case 2: n < 0

Prime loop skipped.

---

## Case 3: Large n

Execution slower due to prime checking.

---

# Possible Improvements

- Use optimized prime checking
- Use Runnable interface
- Add thread synchronization

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. Logical Error

Without:
```java
if(n<2)
```

1 may incorrectly appear prime.

---

# Viva Questions

## Q1. What is thread?
Lightweight subprocess.

---

## Q2. Which class is used for multithreading?

```java
Thread
```

---

## Q3. Which method starts thread?

```java
start()
```

---

## Q4. Which method contains thread code?

```java
run()
```

---

## Q5. Difference between start() and run()?

| start() | run() |
|---|---|
| Creates new thread | Normal method call |

---

## Q6. What is multithreading?
Executing multiple threads simultaneously.

---

## Q7. What is prime number?
Number with exactly 2 factors.

---

## Q8. Why override run()?
To define thread task.

---

## Q9. What is concurrency?
Multiple tasks executing together.

---

## Q10. What is time complexity for prime generation?

:contentReference[oaicite:3]{index=3}