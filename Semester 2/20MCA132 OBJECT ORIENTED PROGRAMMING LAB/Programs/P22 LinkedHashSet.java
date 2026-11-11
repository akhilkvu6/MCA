import java.util.*;

public class P22_LinkedHashSet
{
    public static void main(String[] args)
    {
        Set<String> set=new LinkedHashSet<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1: Add\n2: Remove\n3: Display\n4: Search\n5: Size\n6: Clear\n0: Exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    set.add(el);
                    break;

                case 2:
                    System.out.print("Enter element to remove: ");
                    el=sc.next();
                    boolean removed=set.remove(el);
                    System.out.println("Element removed: "+removed);
                    break;

                case 3:
                    System.out.println("LinkedHashSet: "+set);
                    break;

                case 4:
                    System.out.print("Enter element to search: ");
                    el=sc.next();
                    boolean contains=set.contains(el);
                    System.out.println("Set contains "+el+" : "+contains);
                    break;

                case 5:
                    System.out.println("Size of set: "+set.size());
                    break;

                case 6:
                    set.clear();
                    System.out.println("Set cleared");
                    break;

                case 0:
                    System.out.println("Exiting");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        }while(ch!=0);
    }
}