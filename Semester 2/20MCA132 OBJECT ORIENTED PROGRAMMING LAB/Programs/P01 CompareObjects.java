// Program 1: Define a class Product with data members pcode, pname, price. Create 3 objects of the class and find the product having the lowest price.

import java.util.Scanner;

class Product
{
    String pcode, pname;
    int price;

    void details(int n)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("\nEnter product code for item " + n + ": ");
        pcode = sc.next();

        System.out.print("Enter product name for item " + n + ": ");
        pname = sc.next();

        System.out.print("Enter product price for item " + n + ": ");
        price = sc.nextInt();
    }

    void lowest(Product a, Product b)
    {
        if(price < a.price && price < b.price)
        {
            System.out.println("\nProduct " + pname + " has lowest price");
        }
        else if(a.price < b.price)
        {
            System.out.println("\nProduct " + a.pname + " has lowest price");
        }
        else
        {
            System.out.println("\nProduct " + b.pname + " has lowest price");
        }
    }
}

public class P01_CompareObjects
{
    public static void main(String[] args)
    {
        Product p1 = new Product();
        Product p2 = new Product();
        Product p3 = new Product();

        p1.details(1);
        p2.details(2);
        p3.details(3);

        p1.lowest(p2, p3);
    }
}