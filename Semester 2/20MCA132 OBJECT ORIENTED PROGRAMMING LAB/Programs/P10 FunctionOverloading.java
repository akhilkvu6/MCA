// Program 10: Calculate area of different shapes using function overloading.

import java.util.Scanner;

class ShapeArea
{
    void area(double r)
    {
        System.out.println("Area of circle: " + String.format("%.2f", 3.14 * r * r));
    }

    void area(float r)
    {
        System.out.println("Area of square: " + (r * r));
    }

    void area(double l, double b)
    {
        System.out.println("Area of rectangle: " + (l * b));
    }

    void area(float b, float h)
    {
        System.out.println("Area of triangle: " + (0.5 * b * h));
    }
}

public class P10_FunctionOverloading
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        ShapeArea s = new ShapeArea();

        System.out.print("Enter radius of circle: ");
        s.area(sc.nextDouble());

        System.out.print("Enter length of side of square: ");
        s.area(sc.nextFloat());

        System.out.print("Enter length and breadth of rectangle: ");
        double l = sc.nextDouble();
        double b = sc.nextDouble();

        s.area(l, b);

        System.out.print("Enter breadth and height of triangle: ");
        float b1 = sc.nextFloat();
        float h = sc.nextFloat();

        s.area(b1, h);
    }
}