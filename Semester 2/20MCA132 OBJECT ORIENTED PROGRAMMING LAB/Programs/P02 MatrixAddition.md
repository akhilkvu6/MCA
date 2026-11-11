# Program 2 - Matrix Addition

## Question

Read 2 matrices from the console and perform matrix addition.

---

# Filename

```text
P2_MatrixAddition.java
```

---

# Source Code

```java
// Program 2: Read 2 matrices from the console and perform matrix addition.

import java.util.Scanner;

class AddMatrix
{
    Scanner sc = new Scanner(System.in);

    int rows, columns;
    int matrix[][];

    AddMatrix(int n)
    {
        System.out.print("Enter size of matrix " + n + ": ");
        rows = sc.nextInt();
        columns = sc.nextInt();

        matrix = new int[rows][columns];

        System.out.println("Enter value of matrix " + n + ": ");

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                matrix[i][j] = sc.nextInt();
            }
        }
    }

    void add(AddMatrix b)
    {
        if(rows != b.rows || columns != b.columns)
        {
            System.out.println("Addition of matrix not possible");
        }
        else
        {
            for(int i = 0; i < rows; i++)
            {
                for(int j = 0; j < columns; j++)
                {
                    matrix[i][j] += b.matrix[i][j];
                }
            }

            System.out.println("Sum of matrix:");
            this.display();
        }
    }

    void display()
    {
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                System.out.print(matrix[i][j] + " ");
            }

            System.out.println();
        }
    }
}

public class P2_MatrixAddition
{
    public static void main(String[] args)
    {
        AddMatrix a = new AddMatrix(1);
        AddMatrix b = new AddMatrix(2);

        a.add(b);
    }
}
```

---

# Concepts Used

- Class
- Object
- Constructor
- Parameterized Constructor
- 2D Array
- Nested Loops
- Object Passing
- Scanner Class
- Matrix Addition
- Encapsulation

---

# Theory

A matrix is a rectangular arrangement of elements in rows and columns.

Matrix addition is possible only when:
- number of rows are equal
- number of columns are equal

The corresponding elements of both matrices are added.

Example:

```text
1 2       4 5       5 7
3 4   +   6 7   =   9 11
```

---

# Detailed Explanation

## AddMatrix Class

The `AddMatrix` class stores:
- matrix dimensions
- matrix elements

Each object represents one matrix.

---

## Instance Variables

```java
int rows, columns;
int matrix[][];
```

| Variable | Description |
|---|---|
| `rows` | Number of rows |
| `columns` | Number of columns |
| `matrix[][]` | Stores matrix elements |

---

# Constructor

```java
AddMatrix(int n)
```

Parameterized constructor used to:
- read matrix size
- create matrix
- read matrix elements

Parameter:
```text
n
```

represents matrix number.

Example:
```text
Enter size of matrix 1
```

---

# Matrix Creation

```java
matrix = new int[rows][columns];
```

Creates a 2D array dynamically.

---

# Nested Loops

```java
for(int i = 0; i < rows; i++)
{
    for(int j = 0; j < columns; j++)
```

Used for:
- row traversal
- column traversal

---

# add() Method

```java
void add(AddMatrix b)
```

This method:
- checks matrix compatibility
- performs matrix addition
- displays sum matrix

---

# Compatibility Check

```java
if(rows != b.rows || columns != b.columns)
```

Checks whether:
- row counts match
- column counts match

If not:
```text
Addition not possible
```

---

# Matrix Addition Logic

```java
matrix[i][j] += b.matrix[i][j];
```

Equivalent to:

```java
matrix[i][j] = matrix[i][j] + b.matrix[i][j];
```

Adds corresponding elements.

---

# display() Method

Displays matrix elements row by row.

---

# Detailed Algorithm

1. Create class named `AddMatrix`.

2. Declare variables:
   - `rows`
   - `columns`
   - `matrix[][]`

3. Declare parameterized constructor:
```java
AddMatrix(int n)
```

4. Read:
   - number of rows
   - number of columns

5. Create matrix using:
```java
new int[rows][columns]
```

6. Read matrix elements using nested loops.

7. Declare method:
```java
add(AddMatrix b)
```

8. Check whether matrix dimensions are equal.

9. If dimensions are not equal:
   - display message
   - terminate addition

10. Otherwise:
   - traverse matrices using nested loops
   - add corresponding elements

11. Store result in current matrix.

12. Call:
```java
display()
```

13. Print sum matrix.

14. Create two matrix objects:
   - `a`
   - `b`

15. Read both matrices.

16. Call:
```java
a.add(b);
```

17. Display result.

18. Stop program.

---

# Flow of Execution

```text
Start Program
      ↓
Create Matrix 1
      ↓
Read Matrix 1 Elements
      ↓
Create Matrix 2
      ↓
Read Matrix 2 Elements
      ↓
Check Matrix Compatibility
      ↓
Perform Matrix Addition
      ↓
Display Sum Matrix
      ↓
Stop Program
```

---

# Dry Run

Suppose:

## Matrix 1

```text
1 2
3 4
```

## Matrix 2

```text
5 6
7 8
```

---

# Addition Process

```text
1 + 5 = 6
2 + 6 = 8
3 + 7 = 10
4 + 8 = 12
```

---

# Sum Matrix

```text
6 8
10 12
```

---

# Sample Input

```text
Enter size of matrix 1: 2 2
Enter value of matrix 1:
1 2
3 4

Enter size of matrix 2: 2 2
Enter value of matrix 2:
5 6
7 8
```

---

# Sample Output

```text
Sum of matrix:
6 8
10 12
```

---

# Edge Cases

## Case 1: Different Matrix Sizes

Input:
```text
2x2 matrix
3x3 matrix
```

Output:
```text
Addition of matrix not possible
```

---

## Case 2: Negative Numbers

Input:
```text
-1 -2
3 4
```

Program still works correctly.

---

## Case 3: Zero Matrix

Input:
```text
0 0
0 0
```

Output remains same as other matrix.

---

# Internal Working

When:
```java
a.add(b);
```

is called:

| Variable | Represents |
|---|---|
| `matrix[][]` | Matrix of object `a` |
| `b.matrix[][]` | Matrix of object `b` |

The method compares:
- row size
- column size

Then performs element-wise addition.

---

# Limitations

Current program:
- handles only integer matrices
- does not use separate result matrix
- modifies original matrix

---

# Possible Improvements

- Use separate result matrix
- Support floating point matrices
- Add matrix subtraction
- Add matrix multiplication
- Add matrix transpose

---

# Time Complexity

For matrix traversal:

:contentReference[oaicite:0]{index=0}

because every element is visited once.

---

# Space Complexity

:contentReference[oaicite:1]{index=1}

for storing matrix elements.

---

# Possible Errors

## 1. InputMismatchException

Occurs when non-integer value is entered.

Example:
```text
a
```

instead of integer.

---

## 2. ArrayIndexOutOfBoundsException

May occur if loop limits are incorrect.

---

## 3. Missing Import Statement

If:
```java
import java.util.Scanner;
```

is removed.

Error:
```text
Scanner cannot be resolved to a type
```

---

# Viva Questions

## Q1. What is a matrix?
A matrix is a rectangular arrangement of elements in rows and columns.

## Q2. When is matrix addition possible?
When both matrices have same dimensions.

## Q3. Why use 2D arrays?
To store matrix elements.

## Q4. What are nested loops?
Loops inside another loop.

## Q5. What is a constructor?
Special method automatically called during object creation.

## Q6. What is parameterized constructor?
Constructor that accepts arguments.

## Q7. Why pass object in add() method?
To access another matrix object.

## Q8. What is dynamic memory allocation?
Memory allocation during runtime.

## Q9. Why use this.display()?
To call current object's display method.

## Q10. What is time complexity of matrix addition?

:contentReference[oaicite:2]{index=2}