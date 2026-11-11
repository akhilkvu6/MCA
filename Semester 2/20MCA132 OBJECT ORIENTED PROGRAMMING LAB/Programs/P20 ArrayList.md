# Program 20 - ArrayList

## Question

Program to maintain a list of Strings using ArrayList from collection framework and perform built-in operations.

---

# Filename

```text
P20_ArrayList.java
```

---

# Source Code

```java
import java.util.*;

public class P20_ArrayList
{
    public static void main(String[] args)
    {
        ArrayList<String> list=new ArrayList<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1: add\n2: size\n3: search by index\n4: find index\n5: contains\n6: remove\n7: remove by index\n8: display\n9: clear\n0: Exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    list.add(el);
                    break;

                case 2:
                    System.out.println("Size of the ArrayList: "+list.size());
                    break;

                case 3:
                    System.out.print("Enter index of element to search: ");
                    int index=sc.nextInt();
                    System.out.println("Element at index "+index+" is "+list.get(index));
                    break;

                case 4:
                    System.out.print("Enter an element to find index: ");
                    el=sc.next();
                    index=list.indexOf(el);
                    System.out.println("Index of "+el+" is "+index);
                    break;

                case 5:
                    System.out.print("Enter an element: ");
                    el=sc.next();
                    boolean contains=list.contains(el);
                    System.out.println(el+" is in the list: "+contains);
                    break;

                case 6:
                    System.out.print("Enter the element to be removed: ");
                    el=sc.next();
                    boolean removed=list.remove(el);
                    System.out.println("After removing "+el+" ArrayList: "+list);
                    break;

                case 7:
                    System.out.print("Enter the index to remove the element: ");
                    index=sc.nextInt();
                    list.remove(index);
                    System.out.println("After removing the element, ArrayList: "+list);
                    break;

                case 8:
                    System.out.println("ArrayList: "+list);
                    break;

                case 9:
                    list.clear();
                    System.out.println("ArrayList cleared");
                    break;

                case 0:
                    System.out.println("Exiting...");
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

- Collection Framework
- ArrayList
- Dynamic Arrays
- Menu Driven Program
- Built-in Methods
- Loops
- Switch Case
- Scanner Class

---

# Theory

Collection Framework in Java provides:
```text
ready-made data structures
```

ArrayList is:
```text
dynamic array implementation
```

provided in:
```java
java.util
```

package.

---

# ArrayList

```java
ArrayList<String>
```

stores:
```text
list of strings dynamically
```

Unlike arrays:
```text
size can grow or shrink dynamically
```

---

# Features of ArrayList

- Dynamic size
- Fast random access
- Built-in methods
- Easy insertion/deletion

---

# Built-in Methods Used

| Method | Purpose |
|---|---|
| add() | Add element |
| size() | Find size |
| get() | Access element |
| indexOf() | Find index |
| contains() | Search element |
| remove() | Delete element |
| clear() | Remove all elements |

---

# add() Method

```java
list.add(el)
```

Adds element into ArrayList.

---

# size() Method

```java
list.size()
```

Returns:
```text
number of elements
```

---

# get() Method

```java
list.get(index)
```

Returns:
```text
element at given index
```

---

# indexOf() Method

```java
list.indexOf(el)
```

Returns:
```text
index of element
```

---

# contains() Method

```java
list.contains(el)
```

Returns:
- true
- false

depending on presence of element.

---

# remove() Method

Two versions:
- remove(element)
- remove(index)

---

# clear() Method

```java
list.clear()
```

Removes:
```text
all elements
```

---

# Menu Driven Program

Program repeatedly displays:
```text
menu options
```

until user chooses:
```text
Exit
```

---

# Detailed Algorithm

1. Create:
```java
ArrayList<String>
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

5. Read choice.

6. Use:
```java
switch
```

statement.

7. Case 1:
   - add element

8. Case 2:
   - display size

9. Case 3:
   - search using index

10. Case 4:
   - find index of element

11. Case 5:
   - check contains

12. Case 6:
   - remove element

13. Case 7:
   - remove by index

14. Case 8:
   - display list

15. Case 9:
   - clear list

16. Case 0:
   - exit loop

17. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create ArrayList
   ↓
Display Menu
   ↓
Read Choice
   ↓
Perform Operation
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

8
```

---

# Sample Output

```text
ArrayList: [Apple, Orange]
```

---

# Dry Run

Add:
```text
Apple
```

List:
```text
[Apple]
```

Add:
```text
Orange
```

List:
```text
[Apple, Orange]
```

Remove:
```text
Apple
```

List:
```text
[Orange]
```

---

# Internal Working

ArrayList internally uses:
```text
dynamic array
```

When capacity full:
```text
new larger array created
```

Elements copied automatically.

---

# Time Complexity

## Add Operation

:contentReference[oaicite:0]{index=0}

---

## Search Operation

:contentReference[oaicite:1]{index=1}

---

## Remove Operation

:contentReference[oaicite:2]{index=2}

---

## Access Using Index

:contentReference[oaicite:3]{index=3}

---

# Space Complexity

:contentReference[oaicite:4]{index=4}

---

# Advantages

- Dynamic resizing
- Easy operations
- Built-in methods
- Flexible data handling

---

# Limitations

- Slower insertion/deletion in middle
- Not synchronized

---

# Edge Cases

## Case 1: Invalid Index

Throws:
```text
IndexOutOfBoundsException
```

---

## Case 2: Empty ArrayList

Display:
```text
[]
```

---

## Case 3: Duplicate Elements

Allowed.

---

# Possible Improvements

- Add exception handling
- Add sorting operation
- Add searching menu

---

# Possible Errors

## 1. InputMismatchException

Occurs for invalid datatype input.

---

## 2. IndexOutOfBoundsException

Occurs for invalid index.

---

# Viva Questions

## Q1. What is ArrayList?
Dynamic array class in Java.

---

## Q2. Which package contains ArrayList?

```java
java.util
```

---

## Q3. Difference between array and ArrayList?

| Array | ArrayList |
|---|---|
| Fixed size | Dynamic size |

---

## Q4. Which method adds element?

```java
add()
```

---

## Q5. Which method removes all elements?

```java
clear()
```

---

## Q6. Which method checks element existence?

```java
contains()
```

---

## Q7. Which method returns size?

```java
size()
```

---

## Q8. Which method finds index?

```java
indexOf()
```

---

## Q9. Time complexity of search?

:contentReference[oaicite:5]{index=5}

---

## Q10. Space complexity?

:contentReference[oaicite:6]{index=6}