// Program 7: Perform string manipulation using Java string functions.

import java.util.Scanner;

public class P07_StringManipulation
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