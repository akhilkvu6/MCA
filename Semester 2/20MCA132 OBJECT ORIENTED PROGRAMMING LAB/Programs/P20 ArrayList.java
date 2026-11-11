import java.util.*;

public class P20_ArrayList
{
    public static void main(String[] args)
    {
        ArrayList<String> list=new ArrayList<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1: add\n2: size\n3: search by index\n4: find index\n5: contains\n6: remove\n7: remove by index\n8: display\n9: clear\n0: Exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    list.add(el);
                    break;

                case 2:
                    System.out.println("Size of the ArrayList: "+list.size());
                    break;

                case 3:
                    System.out.print("Enter index of element to search: ");
                    int index=sc.nextInt();
                    System.out.println("Element at index "+index+" is "+list.get(index));
                    break;

                case 4:
                    System.out.print("Enter an element to find index: ");
                    el=sc.next();
                    index=list.indexOf(el);
                    System.out.println("Index of "+el+" is "+index);
                    break;

                case 5:
                    System.out.print("Enter an element: ");
                    el=sc.next();
                    boolean contains=list.contains(el);
                    System.out.println(el+" is in the list: "+contains);
                    break;

                case 6:
                    System.out.print("Enter the element to be removed: ");
                    el=sc.next();
                    boolean removed=list.remove(el);
                    System.out.println("After removing "+el+" ArrayList: "+list);
                    break;

                case 7:
                    System.out.print("Enter the index to remove the element: ");
                    index=sc.nextInt();
                    list.remove(index);
                    System.out.println("After removing the element, ArrayList: "+list);
                    break;

                case 8:
                    System.out.println("ArrayList: "+list);
                    break;

                case 9:
                    list.clear();
                    System.out.println("ArrayList cleared");
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        }while(ch!=0);
    }
}