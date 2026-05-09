# Program 19 - Generic Stack

## Question

Program to create a generic stack and do the Push and Pop operations.

---

# Filename

```text
P19_GenericStack.java
```

---

# Source Code

```java
import java.util.*;

class stack<T>
{
    ArrayList<T> A;

    int top=-1;

    int size;

    stack(int size)
    {
        this.size=size;

        this.A=new ArrayList<T>(size);
    }

    void push(T X)
    {
        if(top+1==size)
        {
            System.out.println("Stack Overflow");
        }

        else
        {
            top=top+1;

            if(A.size()>top)
            {
                A.set(top,X);
            }

            else
            {
                A.add(X);
            }
        }
    }

    T top()
    {
        if(top==-1)
        {
            System.out.println("Stack Underflow");

            return null;
        }

        else
        {
            return A.get(top);
        }
    }

    void pop()
    {
        if(top==-1)
        {
            System.out.println("Stack Underflow");
        }

        else
        {
            top--;
        }
    }

    boolean empty()
    {
        return top==-1;
    }

    public String toString()
    {
        String Ans="";

        for(int i=0;i<top;i++)
        {
            Ans+=String.valueOf(A.get(i))+"->";
        }

        Ans+=String.valueOf(A.get(top));

        return Ans;
    }
}

public class P19_GenericStack
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        System.out.print("Enter max size of stack: ");

        int n=sc.nextInt();

        stack<Integer> s1=new stack<>(n);

        int v;

        for(int i=0;i<n;i++)
        {
            System.out.print("Enter element "+(i+1)+": ");

            v=sc.nextInt();

            s1.push(v);
        }

        System.out.println("\nStack after pushing "+n+" elements :\n"+s1);

        s1.pop();

        System.out.println("\nStack after pop :\n"+s1);
    }
}
```

---

# Concepts Used

- Generics
- Stack Data Structure
- ArrayList
- Push Operation
- Pop Operation
- Method Overriding
- toString() Method
- Scanner Class
- Object Oriented Programming

---

# Theory

A stack is:
```text
linear data structure
```

which follows:
```text
LIFO (Last In First Out)
```

Principle.

---

# Stack Operations

## Push

Adds element to:
```text
top of stack
```

---

## Pop

Removes element from:
```text
top of stack
```

---

## Top

Returns:
```text
top element
```

without removing it.

---

# Generic Class

```java
class stack<T>
```

represents:
```text
generic stack
```

where:
```text
T can be any datatype
```

Examples:
- Integer
- String
- Double

---

# Advantages of Generics

- Code reusability
- Type safety
- Reduces type casting
- Flexible implementation

---

# ArrayList Used

```java
ArrayList<T>
```

stores stack elements dynamically.

---

# top Variable

```java
int top=-1;
```

Tracks:
```text
topmost index of stack
```

---

# Stack Overflow

Occurs when:
```text
stack becomes full
```

Condition:

:contentReference[oaicite:0]{index=0}

---

# Stack Underflow

Occurs when:
```text
stack is empty
```

Condition:

:contentReference[oaicite:1]{index=1}

---

# push() Method

Adds element into stack.

---

# pop() Method

Removes top element.

---

# empty() Method

Returns:
- true → stack empty
- false → stack not empty

---

# toString() Method

Converts stack into:
```text
string representation
```

Example:

```text
10->20->30
```

---

# Detailed Algorithm

1. Create generic class:
```java
stack<T>
```

2. Declare:
- ArrayList
- top
- size

3. Create constructor.

4. Initialize stack size.

5. Create:
```java
push()
```

method.

6. Check overflow condition.

7. Add element into stack.

8. Create:
```java
top()
```

method.

9. Return top element.

10. Create:
```java
pop()
```

method.

11. Check underflow condition.

12. Remove top element.

13. Create:
```java
empty()
```

method.

14. Create:
```java
toString()
```

method.

15. In main method:
   - read stack size

16. Create stack object.

17. Push elements.

18. Display stack.

19. Pop element.

20. Display updated stack.

21. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Stack Size
   ↓
Create Stack
   ↓
Push Elements
   ↓
Display Stack
   ↓
Pop Element
   ↓
Display Updated Stack
   ↓
Stop
```

---

# Sample Input

```text
Enter max size of stack: 5

Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
Enter element 5: 50
```

---

# Sample Output

```text
Stack after pushing 5 elements :
10->20->30->40->50

Stack after pop :
10->20->30->40
```

---

# Dry Run

Push:
```text
10
20
30
```

Stack:

```text
10->20->30
```

After pop:
```text
10->20
```

Top element removed:
```text
30
```

---

# Internal Working

Stack stores:
```text
elements sequentially
```

top variable controls:
```text
current top position
```

Push:
```text
increments top
```

Pop:
```text
decrements top
```

---

# Time Complexity

## Push Operation

:contentReference[oaicite:2]{index=2}

---

## Pop Operation

:contentReference[oaicite:3]{index=3}

---

## Top Operation

:contentReference[oaicite:4]{index=4}

---

# Space Complexity

:contentReference[oaicite:5]{index=5}

where:
```text
n = stack size
```

---

# Advantages

- Generic implementation
- Efficient operations
- Reusable code
- Dynamic storage using ArrayList

---

# Limitations

- Fixed maximum size
- No automatic resizing

---

# Edge Cases

## Case 1: Stack Overflow

Occurs when stack full.

---

## Case 2: Stack Underflow

Occurs when pop performed on empty stack.

---

## Case 3: Single Element

After pop:
```text
stack becomes empty
```

---

# Possible Improvements

- Dynamic resizing
- Menu driven stack
- Implement peek operation separately

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. Stack Overflow

Occurs when pushing into full stack.

---

## 3. Stack Underflow

Occurs when popping empty stack.

---

# Viva Questions

## Q1. What is stack?
Linear data structure following LIFO.

---

## Q2. What is LIFO?
Last In First Out.

---

## Q3. What is generic class?
Class that works with multiple datatypes.

---

## Q4. Which collection class used here?

```java
ArrayList
```

---

## Q5. What is push operation?
Adds element to stack.

---

## Q6. What is pop operation?
Removes top element.

---

## Q7. What is stack overflow?
Adding element to full stack.

---

## Q8. What is stack underflow?
Removing element from empty stack.

---

## Q9. Time complexity of push?

:contentReference[oaicite:6]{index=6}

---

## Q10. What is space complexity?

:contentReference[oaicite:7]{index=7}