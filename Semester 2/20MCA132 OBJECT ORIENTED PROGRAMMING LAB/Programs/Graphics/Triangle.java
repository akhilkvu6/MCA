package Graphics;

public class Triangle implements Figure
{
    double breadth;
    double height;

    public Triangle(double b,double h)
    {
        breadth = b;
        height = h;
    }

    public void area()
    {
        System.out.println("Area of Triangle: " +
        String.format("%.2f",(0.5 * breadth * height)));
    }
}