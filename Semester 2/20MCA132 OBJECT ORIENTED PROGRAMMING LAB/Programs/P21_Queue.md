# Program 21 - Queue using PriorityQueue

## Question

Program to demonstrate the creation of queue object using the PriorityQueue class.

---

# Filename

```text
P21_Queue.java
```

---

# Source Code

```java
import java.util.*;

public class P21_Queue
{
    public static void main(String[] args)
    {
        PriorityQueue<String> q=new PriorityQueue<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1:add\n2:remove\n3:display\n4:head\n5:poll\n6:size\n7:contains\n8:clear\n0:exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    q.add(el);
                    break;

                case 2:
                    System.out.print("Enter element to remove: ");
                    el=sc.next();
                    boolean removed=q.remove(el);
                    System.out.println("Element removed: "+removed);
                    break;

                case 3:
                    System.out.println("Priority Queue: "+q);
                    break;

                case 4:
                    System.out.println("Head of the queue: "+q.peek());
                    break;

                case 5:
                    System.out.println("Removed element: "+q.poll());
                    break;

                case 6:
                    System.out.println("Size of queue: "+q.size());
                    break;

                case 7:
                    System.out.print("Enter element to search: ");
                    el=sc.next();
                    System.out.println("Contains "+el+": "+q.contains(el));
                    break;

                case 8:
                    q.clear();
                    System.out.println("Queue cleared");
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Wrong choice");
            }

        }while(ch!=0);
    }
}
```

---

# Concepts Used

- Queue Data Structure
- PriorityQueue Class
- Collection Framework
- Built-in Queue Operations
- Menu Driven Program
- Scanner Class
- Java Collections

---

# Theory

Queue is:
```text
linear data structure
```

which follows:
```text
FIFO (First In First Out)
```

Principle.

---

# PriorityQueue

```java
PriorityQueue
```

is a class in:
```java
java.util
```

package.

It stores elements:
```text
according to priority order
```

By default:
```text
ascending order
```

is maintained.

---

# FIFO Principle

Queue follows:

```text
First In First Out
```

Example:

```text
A inserted first
A removed first
```

---

# Priority Queue Ordering

Elements are arranged:
```text
automatically in sorted order
```

---

# Built-in Methods Used

| Method | Purpose |
|---|---|
| add() | Insert element |
| remove() | Remove element |
| peek() | View head |
| poll() | Remove head |
| contains() | Search element |
| size() | Queue size |
| clear() | Remove all elements |

---

# add() Method

```java
q.add(el)
```

Adds element into queue.

---

# remove() Method

```java
q.remove(el)
```

Removes specific element.

---

# peek() Method

```java
q.peek()
```

Returns:
```text
head element
```

without removing it.

---

# poll() Method

```java
q.poll()
```

Removes and returns:
```text
head element
```

---

# contains() Method

Checks:
```text
whether element exists
```

---

# clear() Method

Removes:
```text
all elements
```

---

# Menu Driven Program

Program repeatedly:
```text
displays menu
```

until user chooses:
```text
Exit
```

---

# Detailed Algorithm

1. Create:
```java
PriorityQueue<String>
```

2. Create variables:
- el
- ch

3. Start:
```java
do-while
```

loop.

4. Display menu.

5. Read user choice.

6. Use:
```java
switch
```

statement.

7. Case 1:
   - add element

8. Case 2:
   - remove element

9. Case 3:
   - display queue

10. Case 4:
   - display head element

11. Case 5:
   - poll head element

12. Case 6:
   - display size

13. Case 7:
   - search element

14. Case 8:
   - clear queue

15. Case 0:
   - exit program

16. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create Queue
   ↓
Display Menu
   ↓
Read Choice
   ↓
Perform Queue Operation
   ↓
Display Result
   ↓
Repeat Until Exit
   ↓
Stop
```

---

# Sample Input

```text
1
Apple

1
Orange

1
Banana

3
```

---

# Sample Output

```text
Priority Queue: [Apple, Orange, Banana]
```

---

# Dry Run

Insert:
```text
Apple
```

Queue:
```text
[Apple]
```

Insert:
```text
Orange
```

Queue:
```text
[Apple, Orange]
```

Poll:
```text
Apple removed
```

Queue:
```text
[Orange]
```

---

# Internal Working

PriorityQueue internally uses:
```text
Heap Data Structure
```

Insertion and deletion maintain:
```text
priority ordering
```

---

# Heap Structure

PriorityQueue uses:
```text
Min Heap
```

by default.

Smallest element becomes:
```text
head
```

---

# Time Complexity

## Add Operation

:contentReference[oaicite:0]{index=0}

---

## Remove Operation

:contentReference[oaicite:1]{index=1}

---

## Peek Operation

:contentReference[oaicite:2]{index=2}

---

## Search Operation

:contentReference[oaicite:3]{index=3}

---

# Space Complexity

:contentReference[oaicite:4]{index=4}

---

# Advantages

- Dynamic size
- Automatic sorting
- Efficient insertion/removal
- Built-in implementation

---

# Limitations

- Does not maintain insertion order
- Duplicate priorities may vary in order

---

# Edge Cases

## Case 1: Empty Queue

peek() returns:
```text
null
```

---

## Case 2: Removing Missing Element

remove() returns:
```text
false
```

---

## Case 3: Duplicate Elements

Allowed.

---

# Possible Improvements

- Add exception handling
- Add descending priority queue
- Add custom comparator

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. NullPointerException

Possible for invalid queue operations.

---

# Viva Questions

## Q1. What is queue?
Linear data structure following FIFO.

---

## Q2. What is FIFO?
First In First Out.

---

## Q3. Which package contains PriorityQueue?

```java
java.util
```

---

## Q4. Which method inserts element?

```java
add()
```

---

## Q5. Which method returns head element?

```java
peek()
```

---

## Q6. Difference between peek() and poll()?

| peek() | poll() |
|---|---|
| Only returns head | Removes head |

---

## Q7. Which data structure used internally?
Heap.

---

## Q8. What type of heap used?
Min Heap.

---

## Q9. Time complexity of insertion?

:contentReference[oaicite:5]{index=5}

---

## Q10. Space complexity?

:contentReference[oaicite:6]{index=6}