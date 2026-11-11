# Program 22 - Set using LinkedHashSet

## Question

Program to demonstrate the creation of Set object using the LinkedHashSet class.

---

# Filename

```text
P22_LinkedHashSet.java
```

---

# Source Code

```java
import java.util.*;

public class P22_LinkedHashSet
{
    public static void main(String[] args)
    {
        Set<String> set=new LinkedHashSet<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1: Add\n2: Remove\n3: Display\n4: Search\n5: Size\n6: Clear\n0: Exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    set.add(el);
                    break;

                case 2:
                    System.out.print("Enter element to remove: ");
                    el=sc.next();
                    boolean removed=set.remove(el);
                    System.out.println("Element removed: "+removed);
                    break;

                case 3:
                    System.out.println("LinkedHashSet: "+set);
                    break;

                case 4:
                    System.out.print("Enter element to search: ");
                    el=sc.next();
                    boolean contains=set.contains(el);
                    System.out.println("Set contains "+el+" : "+contains);
                    break;

                case 5:
                    System.out.println("Size of set: "+set.size());
                    break;

                case 6:
                    set.clear();
                    System.out.println("Set cleared");
                    break;

                case 0:
                    System.out.println("Exiting");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        }while(ch!=0);
    }
}
```

---

# Concepts Used

- Set Interface
- LinkedHashSet Class
- Collection Framework
- Built-in Set Operations
- Menu Driven Program
- Scanner Class
- Java Collections

---

# Theory

Set is:
```text
collection of unique elements
```

Duplicate values are:
```text
not allowed
```

---

# LinkedHashSet

```java
LinkedHashSet
```

is a class in:
```java
java.util
```

package.

It:
- stores unique elements
- maintains insertion order

---

# Features of LinkedHashSet

- No duplicate elements
- Maintains insertion order
- Fast searching
- Dynamic size

---

# Set Interface

```java
Set<String>
```

stores:
```text
collection of strings
```

---

# Difference Between HashSet and LinkedHashSet

| HashSet | LinkedHashSet |
|---|---|
| No order maintained | Insertion order maintained |

---

# Built-in Methods Used

| Method | Purpose |
|---|---|
| add() | Add element |
| remove() | Remove element |
| contains() | Search element |
| size() | Number of elements |
| clear() | Remove all elements |

---

# add() Method

```java
set.add(el)
```

Adds:
```text
element into set
```

Duplicate values are ignored.

---

# remove() Method

```java
set.remove(el)
```

Removes:
```text
specified element
```

---

# contains() Method

```java
set.contains(el)
```

Checks:
```text
whether element exists
```

---

# size() Method

Returns:
```text
number of elements
```

---

# clear() Method

Removes:
```text
all elements from set
```

---

# Menu Driven Program

Program repeatedly:
```text
displays menu
```

until user selects:
```text
Exit
```

---

# Detailed Algorithm

1. Create:
```java
LinkedHashSet<String>
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
   - display set

10. Case 4:
   - search element

11. Case 5:
   - display size

12. Case 6:
   - clear set

13. Case 0:
   - exit program

14. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create LinkedHashSet
   ↓
Display Menu
   ↓
Read Choice
   ↓
Perform Set Operation
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
Apple

3
```

---

# Sample Output

```text
LinkedHashSet: [Apple, Orange]
```

Duplicate:
```text
Apple
```

not inserted again.

---

# Dry Run

Insert:
```text
Apple
```

Set:
```text
[Apple]
```

Insert:
```text
Orange
```

Set:
```text
[Apple, Orange]
```

Insert:
```text
Apple
```

Duplicate ignored.

Set:
```text
[Apple, Orange]
```

---

# Internal Working

LinkedHashSet internally uses:
```text
Hash Table + Linked List
```

Hash table provides:
```text
fast searching
```

Linked list maintains:
```text
insertion order
```

---

# Time Complexity

## Add Operation

:contentReference[oaicite:0]{index=0}

---

## Remove Operation

:contentReference[oaicite:1]{index=1}

---

## Search Operation

:contentReference[oaicite:2]{index=2}

---

# Space Complexity

:contentReference[oaicite:3]{index=3}

---

# Advantages

- No duplicate elements
- Maintains insertion order
- Fast operations
- Dynamic collection

---

# Limitations

- More memory usage than HashSet
- Elements must be unique

---

# Edge Cases

## Case 1: Duplicate Element

Ignored automatically.

---

## Case 2: Empty Set

Display:
```text
[]
```

---

## Case 3: Removing Missing Element

remove() returns:
```text
false
```

---

# Possible Improvements

- Add iterator traversal
- Add sorting
- Add exception handling

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. NullPointerException

Possible for invalid operations.

---

# Viva Questions

## Q1. What is Set?
Collection of unique elements.

---

## Q2. Which class maintains insertion order?

```java
LinkedHashSet
```

---

## Q3. Are duplicate elements allowed?
No.

---

## Q4. Which package contains LinkedHashSet?

```java
java.util
```

---

## Q5. Which method adds element?

```java
add()
```

---

## Q6. Which method checks element existence?

```java
contains()
```

---

## Q7. Which method removes all elements?

```java
clear()
```

---

## Q8. Difference between HashSet and LinkedHashSet?

LinkedHashSet maintains insertion order.

---

## Q9. Time complexity of search?

:contentReference[oaicite:4]{index=4}

---

## Q10. Space complexity?

:contentReference[oaicite:5]{index=5}