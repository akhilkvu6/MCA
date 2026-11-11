# Program 4 - Symmetric Matrix

## Question

Read a matrix from the console and check whether it is symmetric or not.

---

# Filename

```text
P4_SymmetricMatrix.java
```

---

# Source Code

```java
// Program 4: Read a matrix from the console and check whether it is symmetric or not.

import java.util.Scanner;

class Symmetric
{
    Scanner sc = new Scanner(System.in);

    int rows, columns;
    int matrix[][];
    int flag = 0;

    Symmetric()
    {
        System.out.print("Enter size of matrix: ");
        rows = sc.nextInt();
        columns = sc.nextInt();

        matrix = new int[rows][columns];

        System.out.println("Enter value of matrix: ");

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                matrix[i][j] = sc.nextInt();
            }
        }
    }

    void transpose()
    {
        if(rows != columns)
        {
            System.out.println("Matrix is not symmetric");
            return;
        }

        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < columns; j++)
            {
                if(matrix[j][i] != matrix[i][j])
                {
                    flag = 1;
                    break;
                }
            }
        }

        if(flag != 1)
        {
            System.out.println("Matrix is symmetric");
        }
        else
        {
            System.out.println("Matrix is not symmetric");
        }
    }
}

public class P4_SymmetricMatrix
{
    public static void main(String[] args)
    {
        Symmetric a = new Symmetric();

        a.transpose();
    }
}
```

---

# Concepts Used

- Class
- Object
- Constructor
- 2D Array
- Nested Loops
- Matrix Transpose
- Conditional Statements
- Scanner Class
- Encapsulation

---

# Theory

A symmetric matrix is a square matrix in which:

:contentReference[oaicite:0]{index=0}

for all values of:
- `i`
- `j`

This means:
- rows and columns are equal
- matrix is equal to its transpose

Example of symmetric matrix:

```text
1 2 3
2 4 5
3 5 6
```

Because:
```text
matrix[0][1] = matrix[1][0]
matrix[0][2] = matrix[2][0]
matrix[1][2] = matrix[2][1]
```

---

# Detailed Explanation

## Symmetric Class

The `Symmetric` class stores:
- matrix dimensions
- matrix elements
- symmetry checking flag

---

# Instance Variables

```java
int rows, columns;
int matrix[][];
int flag = 0;
```

| Variable | Description |
|---|---|
| `rows` | Number of rows |
| `columns` | Number of columns |
| `matrix[][]` | Stores matrix elements |
| `flag` | Tracks whether matrix is symmetric |

---

# Constructor

```java
Symmetric()
```

Constructor used to:
- read matrix size
- create matrix
- read matrix elements

---

# Matrix Creation

```java
matrix = new int[rows][columns];
```

Creates 2D matrix dynamically.

---

# transpose() Method

```java
void transpose()
```

This method checks whether matrix is symmetric.

---

# Symmetric Matrix Condition

A matrix is symmetric only if:

:contentReference[oaicite:1]{index=1}

for every element.

---

# Square Matrix Check

```java
if(rows != columns)
```

Symmetric matrix must always be square matrix.

If:
```text
rows ≠ columns
```

then matrix cannot be symmetric.

---

# Comparison Logic

```java
if(matrix[j][i] != matrix[i][j])
```

Checks:
- upper triangle elements
- lower triangle elements

If any pair differs:
- matrix is not symmetric

---

# Flag Variable

```java
flag = 1;
```

Used to indicate:
```text
Matrix is not symmetric
```

---

# Detailed Algorithm

1. Create class named `Symmetric`.

2. Declare variables:
   - `rows`
   - `columns`
   - `matrix[][]`
   - `flag`

3. Create constructor:
```java
Symmetric()
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
transpose()
```

8. Check whether matrix is square.

9. If matrix is not square:
   - display matrix is not symmetric
   - stop checking

10. Traverse matrix using nested loops.

11. Compare:
```java
matrix[i][j]
```

with:
```java
matrix[j][i]
```

12. If any elements are not equal:
   - set flag = 1
   - break loop

13. After traversal:
   - if flag = 0:
     - matrix is symmetric
   - otherwise:
     - matrix is not symmetric

14. Create object:
```java
Symmetric a
```

15. Call:
```java
a.transpose();
```

16. Display result.

17. Stop program.

---

# Flow of Execution

```text
Start Program
      ↓
Read Matrix Size
      ↓
Create Matrix
      ↓
Read Matrix Elements
      ↓
Check Square Matrix
      ↓
Compare matrix[i][j] and matrix[j][i]
      ↓
Symmetric ?
      ↓
Display Result
      ↓
Stop Program
```

---

# Dry Run

Suppose matrix:

```text
1 2 3
2 4 5
3 5 6
```

---

# Step 1

Check:

:contentReference[oaicite:2]{index=2}

Result:
```text
2 = 2
```

True.

---

# Step 2

Check:

:contentReference[oaicite:3]{index=3}

Result:
```text
3 = 3
```

True.

---

# Step 3

Check:

:contentReference[oaicite:4]{index=4}

Result:
```text
5 = 5
```

True.

---

# Output

```text
Matrix is symmetric
```

---

# Sample Input

```text
Enter size of matrix: 3 3

Enter value of matrix:
1 2 3
2 4 5
3 5 6
```

---

# Sample Output

```text
Matrix is symmetric
```

---

# Edge Cases

## Case 1: Non-Square Matrix

Input:
```text
2 x 3 matrix
```

Output:
```text
Matrix is not symmetric
```

---

## Case 2: Non-Symmetric Matrix

Input:

```text
1 2
3 4
```

Because:
```text
matrix[0][1] ≠ matrix[1][0]
```

Output:
```text
Matrix is not symmetric
```

---

## Case 3: Identity Matrix

Input:

```text
1 0 0
0 1 0
0 0 1
```

Identity matrix is always symmetric.

---

# Internal Working

The program compares:
- upper triangular elements
with
- lower triangular elements

using:

:contentReference[oaicite:5]{index=5}

If all comparisons are true:
- matrix is symmetric.

---

# Limitations

Current program:
- handles only integer matrices
- checks full matrix unnecessarily
- does not use separate transpose matrix

---

# Possible Improvements

- Check only upper triangular matrix
- Create transpose matrix separately
- Support floating point matrices
- Add transpose display

---

# Time Complexity

For matrix traversal:

:contentReference[oaicite:6]{index=6}

because every element may be checked.

---

# Space Complexity

:contentReference[oaicite:7]{index=7}

for storing matrix.

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

May occur if loop conditions are incorrect.

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

## Q1. What is a symmetric matrix?

A matrix satisfying:

:contentReference[oaicite:8]{index=8}

---

## Q2. Can rectangular matrix be symmetric?
No. Symmetric matrix must be square.

---

## Q3. What is transpose of matrix?
Interchanging rows and columns.

---

## Q4. Why use nested loops?
To traverse matrix rows and columns.

---

## Q5. What is 2D array?
Array containing rows and columns.

---

## Q6. What is purpose of flag variable?
To indicate whether matrix is symmetric.

---

## Q7. Why check rows != columns?
Symmetric matrix must have same rows and columns.

---

## Q8. What is constructor?
Special method automatically called during object creation.

---

## Q9. What is time complexity?

:contentReference[oaicite:9]{index=9}

---

## Q10. What is space complexity?

:contentReference[oaicite:10]{index=10}