// Program 3: Read 2 complex numbers and perform addition on the 2 complex numbers.

import java.util.Scanner;

class Complex
{
    int real, imaginary;

    Scanner sc = new Scanner(System.in);

    void input(int n)
    {
        System.out.print("\nEnter real part of the number " + n + ": ");
        real = sc.nextInt();

        System.out.print("Enter imaginary part of the number " + n + ": ");
        imaginary = sc.nextInt();
    }

    void add(Complex b)
    {
        Complex c = new Complex();

        c.real = real + b.real;
        c.imaginary = imaginary + b.imaginary;

        System.out.println("\n(" + real + " + i" + imaginary + ") + (" + b.real + " + i" + b.imaginary + ") = "+ c.real + " + i" + c.imaginary);
    }
}

public class P03_ComplexNumberAddition
{
    public static void main(String[] args)
    {
        Complex a = new Complex();
        Complex b = new Complex();

        a.input(1);
        b.input(2);

        a.add(b);
    }
}