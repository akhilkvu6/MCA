import java.util.*;

public class P21_Queue
{
    public static void main(String[] args)
    {
        PriorityQueue<String> q=new PriorityQueue<String>();

        Scanner sc=new Scanner(System.in);

        String el;

        int ch;

        do
        {
            System.out.print("\n----------------\n1:add\n2:remove\n3:display\n4:head\n5:poll\n6:size\n7:contains\n8:clear\n0:exit\n----------------\nEnter your choice: ");

            ch=sc.nextInt();

            switch(ch)
            {
                case 1:
                    System.out.print("Enter element to insert: ");
                    el=sc.next();
                    q.add(el);
                    break;

                case 2:
                    System.out.print("Enter element to remove: ");
                    el=sc.next();
                    boolean removed=q.remove(el);
                    System.out.println("Element removed: "+removed);
                    break;

                case 3:
                    System.out.println("Priority Queue: "+q);
                    break;

                case 4:
                    System.out.println("Head of the queue: "+q.peek());
                    break;

                case 5:
                    System.out.println("Removed element: "+q.poll());
                    break;

                case 6:
                    System.out.println("Size of queue: "+q.size());
                    break;

                case 7:
                    System.out.print("Enter element to search: ");
                    el=sc.next();
                    System.out.println("Contains "+el+": "+q.contains(el));
                    break;

                case 8:
                    q.clear();
                    System.out.println("Queue cleared");
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Wrong choice");
            }

        }while(ch!=0);
    }
}