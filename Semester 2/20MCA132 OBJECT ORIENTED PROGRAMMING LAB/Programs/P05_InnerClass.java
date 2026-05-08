// Program 5: Create CPU with attribute price. Create inner class Processor and static nested class RAM.

import java.util.Scanner;

class CPU
{
    Scanner sc = new Scanner(System.in);

    int price;

    class Processor
    {
        int noOfCores;
        String manufacturer;

        Processor()
        {
            System.out.print("Enter number of cores in the processor: ");
            noOfCores = sc.nextInt();

            System.out.print("Enter manufacturer of the processor: ");
            manufacturer = sc.next();
        }
    }

    static class RAM
    {
        Scanner sc = new Scanner(System.in);

        int memory;
        String manufacturer;

        RAM()
        {
            System.out.print("Enter memory capacity of RAM: ");
            memory = sc.nextInt();

            System.out.print("Enter manufacturer of the RAM: ");
            manufacturer = sc.next();
        }
    }
}

public class P5_InnerClass
{
    public static void main(String[] args)
    {
        CPU c = new CPU();

        CPU.Processor p = c.new Processor();

        CPU.RAM r = new CPU.RAM();

        c.price = 2500 + (p.noOfCores * 20) + (r.memory * 15);

        System.out.println("\nProcessor Details");
        System.out.println("Number of Cores: " + p.noOfCores);
        System.out.println("Manufacturer: " + p.manufacturer);

        System.out.println("\nRAM Details");
        System.out.println("Memory Capacity: " + r.memory + " GB");
        System.out.println("Manufacturer: " + r.manufacturer);

        System.out.println("\nCPU Price: " + c.price);
    }
}