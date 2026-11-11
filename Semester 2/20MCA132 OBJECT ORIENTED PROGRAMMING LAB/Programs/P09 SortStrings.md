# Program 9 - Sort Strings

## Question

Write a Java program to sort strings.

---

# Filename

```text
P9_SortStrings.java
```

---

# Source Code

```java
// Program 9: Sort strings using Bubble Sort.

import java.util.Scanner;

class SortStrings
{
    Scanner sc = new Scanner(System.in);

    String s[];
    int size;

    SortStrings()
    {
        System.out.print("Enter no: of strings: ");
        size = sc.nextInt();

        s = new String[size];

        System.out.println("Enter " + size + " strings:");

        for(int i = 0; i < size; i++)
        {
            s[i] = sc.next();
        }
    }

    void sort()
    {
        for(int i = 0; i < size; i++)
        {
            for(int j = 0; j < size - i - 1; j++)
            {
                if(s[j].compareTo(s[j + 1]) > 0)
                {
                    String temp = s[j];

                    s[j] = s[j + 1];

                    s[j + 1] = temp;
                }
            }
        }
    }

    void display()
    {
        for(int i = 0; i < size; i++)
        {
            System.out.print(s[i] + " ");
        }
    }
}

public class P9_SortStrings
{
    public static void main(String[] args)
    {
        SortStrings s1 = new SortStrings();

        System.out.println("\nOriginal String Array");
        s1.display();

        s1.sort();

        System.out.println("\n\nSorted String Array");
        s1.display();
    }
}
```

---

# Concepts Used

- Class
- Object
- Array of Strings
- Bubble Sort
- String Comparison
- compareTo() Method
- Nested Loops
- Scanner Class

---

# Theory

Sorting means:
```text
arranging data in a particular order
```

This program sorts:
```text
strings in alphabetical order
```

using:
```text
Bubble Sort Algorithm
```

Java provides:
```java
compareTo()
```

method to compare strings lexicographically.

---

# Bubble Sort

Bubble Sort repeatedly:
- compares adjacent elements
- swaps them if they are in wrong order

Largest element moves toward end after each pass.

---

# compareTo() Method

```java
s1.compareTo(s2)
```

returns:

| Value | Meaning |
|---|---|
| Positive | s1 > s2 |
| Negative | s1 < s2 |
| Zero | Both strings equal |

---

# Example

```java
"cat".compareTo("bat")
```

returns:
```text
positive value
```

because:
```text
cat > bat
```

alphabetically.

---

# Detailed Explanation

## String Array

```java
String s[];
```

Stores multiple strings.

---

# Constructor

```java
SortStrings()
```

Used to:
- read size
- create string array
- read strings

---

# Reading Strings

```java
s[i] = sc.next();
```

Reads individual strings.

---

# Sorting Logic

```java
if(s[j].compareTo(s[j + 1]) > 0)
```

Checks whether:
```text
left string > right string
```

If true:
- swap strings

---

# Swapping

```java
String temp = s[j];
s[j] = s[j + 1];
s[j + 1] = temp;
```

Used to exchange positions.

---

# Nested Loops

Outer loop:
```text
controls passes
```

Inner loop:
```text
compares adjacent elements
```

---

# display() Method

Displays array elements.

---

# Detailed Algorithm

1. Create class:
```java
SortStrings
```

2. Declare:
```java
String s[]
```

and:
```java
size
```

3. Create constructor.

4. Read number of strings.

5. Create string array.

6. Read strings into array.

7. Create method:
```java
sort()
```

8. Use nested loops.

9. Compare adjacent strings using:
```java
compareTo()
```

10. If strings are in wrong order:
   - swap them

11. Repeat until array sorted.

12. Create:
```java
display()
```

method.

13. Print original array.

14. Call:
```java
sort()
```

15. Print sorted array.

16. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Number of Strings
   ↓
Read String Array
   ↓
Display Original Array
   ↓
Compare Adjacent Strings
   ↓
Swap if Needed
   ↓
Repeat Sorting
   ↓
Display Sorted Array
   ↓
Stop
```

---

# Dry Run

Input:

```text
dog
apple
cat
```

---

# Pass 1

Compare:
```text
dog > apple
```

Swap.

Array:
```text
apple dog cat
```

---

Compare:
```text
dog > cat
```

Swap.

Array:
```text
apple cat dog
```

---

# Pass 2

Compare:
```text
apple > cat
```

False.

No swap.

---

# Sorted Array

```text
apple cat dog
```

---

# Sample Input

```text
Enter no: of strings: 4

Enter 4 strings:
dog
apple
cat
ball
```

---

# Sample Output

```text
Original String Array
dog apple cat ball

Sorted String Array
apple ball cat dog
```

---

# Edge Cases

## Case 1: Already Sorted

Input:
```text
apple ball cat dog
```

No swaps required.

---

## Case 2: Duplicate Strings

Input:
```text
apple apple cat
```

Duplicates remain.

---

## Case 3: Single String

Input:
```text
hello
```

Already sorted.

---

## Case 4: Empty Array

Input:
```text
0
```

No strings stored.

---

# Internal Working

Program performs:
```text
lexicographical comparison
```

using:
```java
compareTo()
```

Sorting performed using:
```text
Bubble Sort
```

---

# Time Complexity

Worst Case:

:contentReference[oaicite:0]{index=0}

because nested loops are used.

---

# Best Case Complexity

Optimized Bubble Sort:

:contentReference[oaicite:1]{index=1}

Current implementation still runs:

:contentReference[oaicite:2]{index=2}

---

# Space Complexity

:contentReference[oaicite:3]{index=3}

only temporary variable used.

---

# Advantages

- Simple sorting algorithm
- Easy implementation
- Useful for small datasets

---

# Limitations

- Slow for large data
- Multiple comparisons
- Inefficient compared to advanced sorting algorithms

---

# Possible Improvements

- Use optimized Bubble Sort
- Use Arrays.sort()
- Use quick sort or merge sort

---

# Possible Errors

## 1. InputMismatchException

Occurs if invalid input entered.

---

## 2. NullPointerException

Occurs if strings not initialized.

---

## 3. Empty Strings

May affect sorting order.

---

# Viva Questions

## Q1. What is sorting?
Arranging data in order.

---

## Q2. Which sorting algorithm is used?
Bubble Sort.

---

## Q3. What does compareTo() do?
Compares two strings lexicographically.

---

## Q4. What happens if compareTo() returns positive value?
First string is greater.

---

## Q5. What is lexicographical order?
Dictionary order.

---

## Q6. What is time complexity of Bubble Sort?

:contentReference[oaicite:4]{index=4}

---

## Q7. What is space complexity?

:contentReference[oaicite:5]{index=5}

---

## Q8. Why nested loops are used?
To repeatedly compare adjacent elements.

---

## Q9. What is swapping?
Exchanging positions of elements.

---

## Q10. What is string array?
Array storing multiple strings.