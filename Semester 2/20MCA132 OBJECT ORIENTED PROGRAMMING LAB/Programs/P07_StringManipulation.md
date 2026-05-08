# Program 7 - String Manipulation

## Question

Perform string manipulation using Java string functions.

Functions used:

- `toLowerCase()`
- `toUpperCase()`
- `length()`
- `substring()`
- `trim()`
- `indexOf()`
- `concat()`

---

# Filename

```text
P7_StringManipulation.java
```

---

# Source Code

```java
// Program 7: Perform string manipulation using Java string functions.

import java.util.Scanner;

public class P7_StringManipulation
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String s = sc.nextLine();

        System.out.print("Enter another string: ");
        String str2 = sc.nextLine();

        System.out.println("\nLowercase version: " + s.toLowerCase());

        System.out.println("Uppercase version: " + s.toUpperCase());

        System.out.println("Length of string: " + s.length());

        System.out.println("Substring starting from index 2: " + s.substring(2));

        System.out.println("Substring from index 1 to 4: " + s.substring(1, 4));

        System.out.println("Trimmed string: " + s.trim());

        System.out.println("Index of first occurrence of 'a': " + s.indexOf('a'));

        System.out.println("Index of 'a' starting from index 2: " + s.indexOf('a', 2));

        System.out.println("Concatenated string: " + s.concat(str2));
    }
}
```

---

# Concepts Used

- String Class
- String Methods
- User Input
- Scanner Class
- String Manipulation
- Built-in Functions

---

# Theory

A string in Java is a sequence of characters.

Java provides:
```text
String class
```

which contains several built-in methods for manipulating strings.

String functions help to:
- modify strings
- search characters
- extract substrings
- concatenate strings
- convert cases

---

# String Functions Used

| Function | Purpose |
|---|---|
| `toLowerCase()` | Converts string to lowercase |
| `toUpperCase()` | Converts string to uppercase |
| `length()` | Returns length of string |
| `substring()` | Extracts part of string |
| `trim()` | Removes leading and trailing spaces |
| `indexOf()` | Finds index of character |
| `concat()` | Combines two strings |

---

# Detailed Explanation

## Reading Strings

```java
String s = sc.nextLine();
```

Used to read complete string including spaces.

---

# toLowerCase()

```java
s.toLowerCase()
```

Converts all characters to lowercase.

Example:

```text
HELLO → hello
```

---

# toUpperCase()

```java
s.toUpperCase()
```

Converts all characters to uppercase.

Example:

```text
hello → HELLO
```

---

# length()

```java
s.length()
```

Returns total number of characters in string.

Example:

```text
Hello → 5
```

---

# substring(n)

```java
s.substring(2)
```

Returns substring starting from index 2.

Example:

```text
Hello → llo
```

---

# substring(n, m)

```java
s.substring(1, 4)
```

Returns substring from index 1 to 3.

Example:

```text
Hello → ell
```

---

# trim()

```java
s.trim()
```

Removes spaces from beginning and end.

Example:

```text
" Hello " → "Hello"
```

---

# indexOf(char)

```java
s.indexOf('a')
```

Returns index of first occurrence of character.

Example:

```text
banana → 1
```

---

# indexOf(char, i)

```java
s.indexOf('a', 2)
```

Searches from specified index.

Example:

```text
banana → 3
```

---

# concat()

```java
s.concat(str2)
```

Combines two strings.

Example:

```text
Hello + World → HelloWorld
```

---

# Detailed Algorithm

1. Import Scanner class.

2. Create class:
```java
P7_StringManipulation
```

3. Create main method.

4. Create Scanner object.

5. Read first string using:
```java
nextLine()
```

6. Read second string.

7. Convert string to lowercase using:
```java
toLowerCase()
```

8. Convert string to uppercase using:
```java
toUpperCase()
```

9. Find string length using:
```java
length()
```

10. Extract substring using:
```java
substring()
```

11. Remove spaces using:
```java
trim()
```

12. Find character index using:
```java
indexOf()
```

13. Concatenate strings using:
```java
concat()
```

14. Display all outputs.

15. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Read First String
   ↓
Read Second String
   ↓
Perform String Functions
   ↓
Display Results
   ↓
Stop
```

---

# Sample Input

```text
Enter a string: Java Programming

Enter another string: Language
```

---

# Sample Output

```text
Lowercase version: java programming

Uppercase version: JAVA PROGRAMMING

Length of string: 16

Substring starting from index 2: va Programming

Substring from index 1 to 4: ava

Trimmed string: Java Programming

Index of first occurrence of 'a': 1

Index of 'a' starting from index 2: 3

Concatenated string: Java ProgrammingLanguage
```

---

# Edge Cases

## Case 1: Empty String

Input:
```text
""
```

Length becomes:

:contentReference[oaicite:0]{index=0}

---

## Case 2: Character Not Found

```java
indexOf('z')
```

returns:

:contentReference[oaicite:1]{index=1}

---

## Case 3: Invalid Substring Index

```java
substring(5, 20)
```

may cause:
```text
StringIndexOutOfBoundsException
```

---

# Internal Working

Java strings are:
```text
immutable
```

Meaning:
- original string does not change
- methods create new strings

---

# Time Complexity

Most string operations:

:contentReference[oaicite:2]{index=2}

where:
```text
n = length of string
```

---

# Space Complexity

:contentReference[oaicite:3]{index=3}

because new strings are created.

---

# Advantages of String Functions

- Easy manipulation
- Built-in support
- Efficient processing
- Reduces coding complexity

---

# Limitations

- Strings are immutable
- Large operations consume memory

---

# Possible Errors

## 1. StringIndexOutOfBoundsException

Occurs when invalid index is used.

Example:

```java
substring(10)
```

for small string.

---

## 2. NullPointerException

Occurs when string variable is null.

---

# Viva Questions

## Q1. What is a string?
Collection of characters.

---

## Q2. Which class represents strings in Java?
`String` class.

---

## Q3. What is immutability?
String value cannot be modified after creation.

---

## Q4. What does `length()` return?
Number of characters in string.

---

## Q5. What is `substring()`?
Method used to extract part of string.

---

## Q6. What does `trim()` do?
Removes leading and trailing spaces.

---

## Q7. What does `concat()` do?
Combines two strings.

---

## Q8. What is returned if character is not found in `indexOf()`?

:contentReference[oaicite:4]{index=4}

---

## Q9. Difference between `toUpperCase()` and `toLowerCase()`?

| Method | Purpose |
|---|---|
| `toUpperCase()` | Converts to uppercase |
| `toLowerCase()` | Converts to lowercase |

---

## Q10. What is Scanner class?
Used for user input in Java.