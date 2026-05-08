# Program 6 - Search Element In Array

## Question

Program to search for an element in an array.

---

# Filename

```text
P06_SearchElementInArray.java
```

---

# Source Code

```java
// Program 6: Program to search for an element in an array.

import java.util.Scanner;

class Array
{
    Scanner sc = new Scanner(System.in);

    int arr[], size;

    Array(int n)
    {
        size = n;

        arr = new int[n];

        System.out.println("Enter elements to the array:");

        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
    }

    void search(int n)
    {
        int flag = 0;

        for(int i = 0; i < size; i++)
        {
            if(arr[i] == n)
            {
                flag = 1;

                System.out.println(n + " is found in the array.");

                break;
            }
        }

        if(flag == 0)
        {
            System.out.println(n + " is not an element of the array.");
        }
    }
}

public class P06_SearchElementInArray
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter no: of elements in the array: ");
        int n = sc.nextInt();

        Array a = new Array(n);

        System.out.print("Enter number to be searched: ");
        int num = sc.nextInt();

        a.search(num);
    }
}
```

---

# Concepts Used

- Class
- Object
- Array
- Constructor
- Linear Search
- Looping
- Conditional Statements
- Scanner Class

---

# Theory

Searching means:
```text
finding a particular element in a collection of data
```

This program searches for:
```text
an integer element inside an array
```

using:
```text
Linear Search Algorithm
```

---

# Linear Search

Linear search checks:
```text
each element one by one
```

until:
- element is found
OR
- array ends

---

# Array

```java
int arr[]
```

stores multiple integer values.

---

# Constructor

```java
Array(int n)
```

used to:
- initialize array size
- create array
- read array elements

---

# search() Method

```java
void search(int n)
```

searches for:
```text
number n
```

inside array.

---

# Flag Variable

```java
int flag = 0;
```

Used to track:
- element found
- element not found

---

# break Statement

```java
break;
```

stops loop immediately after element is found.

Improves efficiency.

---

# Detailed Algorithm

1. Create class:
```java
Array
```

2. Declare:
```java
arr[]
```

and:
```java
size
```

3. Create constructor:
```java
Array(int n)
```

4. Initialize:
```java
size = n
```

5. Create array of size:
```java
n
```

6. Read array elements.

7. Create method:
```java
search(int n)
```

8. Initialize:
```java
flag = 0
```

9. Traverse array using loop.

10. Compare:
```java
arr[i]
```

with:
```java
n
```

11. If element found:
   - set flag = 1
   - print found message
   - stop loop

12. If flag remains 0:
   - print not found message

13. In main method:
   - read array size
   - create array object
   - read search element
   - call search()

14. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read Array Size
   ↓
Create Array
   ↓
Read Elements
   ↓
Read Search Element
   ↓
Compare Elements One by One
   ↓
Element Found?
   ↓
Display Result
   ↓
Stop
```

---

# Dry Run

Suppose array:

```text
10 20 30 40
```

Search:
```text
30
```

---

# Step 1

Compare:
```text
10 == 30
```

False.

---

# Step 2

Compare:
```text
20 == 30
```

False.

---

# Step 3

Compare:
```text
30 == 30
```

True.

---

# Output

```text
30 is found in the array.
```

---

# Sample Input

```text
Enter no: of elements in the array: 5

Enter elements to the array:
10
20
30
40
50

Enter number to be searched: 40
```

---

# Sample Output

```text
40 is found in the array.
```

---

# Edge Cases

## Case 1: Element Not Found

Input:
```text
99
```

Output:
```text
99 is not an element of the array.
```

---

## Case 2: Empty Array

Input:
```text
0
```

No elements stored.

---

## Case 3: Duplicate Elements

Input:
```text
10 20 20 30
```

Program stops after first occurrence.

---

# Internal Working

Program sequentially checks:
```text
each array element
```

This is:
```text
Linear Search
```

---

# Time Complexity

Worst Case:

:contentReference[oaicite:0]{index=0}

because all elements may need checking.

---

# Best Case Complexity

If element found at beginning:

:contentReference[oaicite:1]{index=1}

---

# Space Complexity

:contentReference[oaicite:2]{index=2}

for storing array elements.

---

# Advantages

- Simple implementation
- Easy to understand
- Works for unsorted arrays

---

# Limitations

- Slow for large arrays
- Inefficient compared to binary search

---

# Possible Improvements

- Use binary search
- Add sorting
- Search multiple elements

---

# Possible Errors

## 1. InputMismatchException

Occurs when invalid datatype entered.

Example:
```text
abc
```

instead of integer.

---

## 2. ArrayIndexOutOfBoundsException

Occurs if index exceeds array size.

---

# Viva Questions

## Q1. What is searching?
Finding an element in data.

---

## Q2. Which searching algorithm is used?
Linear Search.

---

## Q3. What is an array?
Collection of similar datatype elements.

---

## Q4. Why use flag variable?
To track search status.

---

## Q5. What does break do?
Stops loop immediately.

---

## Q6. What is worst-case complexity?

:contentReference[oaicite:3]{index=3}

---

## Q7. What is best-case complexity?

:contentReference[oaicite:4]{index=4}

---

## Q8. Can linear search work on unsorted arrays?
Yes.

---

## Q9. What happens if duplicates exist?
First matching element found.

---

## Q10. What is space complexity?

:contentReference[oaicite:5]{index=5}