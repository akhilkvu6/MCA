#include <stdio.h>

int main()
{
    int arr[100], n, choice, element, pos, key;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    do
    {
        printf("\nArray Operations Menu:\n");
        printf("1. Traverse\n2. Insert\n3. Delete\n4. Search\n5. Update\n6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1: // Traverse
            {
                printf("Array elements: ");
                for(int i = 0; i < n; i++)
                {
                    printf("%d ", arr[i]);
                }
                printf("\n");
                break;
            }

            case 2: // Insert
            {
                printf("Enter element to insert: ");
                scanf("%d", &element);
                printf("Enter position (0-based index): ");
                scanf("%d", &pos);

                if(pos < 0 || pos > n)
                {
                    printf("Invalid position\n");
                }
                else
                {
                    for(int i = n; i > pos; i--)
                    {
                        arr[i] = arr[i - 1];
                    }
                    arr[pos] = element;
                    n++;
                    printf("Element inserted\n");
                }
                break;
            }

            case 3: // Delete
            {
                printf("Enter position to delete (0-based index): ");
                scanf("%d", &pos);

                if(pos < 0 || pos >= n)
                {
                    printf("Invalid position\n");
                }
                else
                {
                    for(int i = pos; i < n - 1; i++)
                    {
                        arr[i] = arr[i + 1];
                    }
                    n--;
                    printf("Element deleted\n");
                }
                break;
            }

            case 4: // Search
            {
                printf("Enter element to search: ");
                scanf("%d", &key);
                pos = -1;

                for(int i = 0; i < n; i++)
                {
                    if(arr[i] == key)
                    {
                        pos = i;
                        break;
                    }
                }

                if(pos != -1)
                {
                    printf("Element found at index %d\n", pos);
                }
                else
                {
                    printf("Element not found\n");
                }
                break;
            }

            case 5: // Update
            {
                printf("Enter position to update (0-based index): ");
                scanf("%d", &pos);

                if(pos < 0 || pos >= n)
                {
                    printf("Invalid position\n");
                }
                else
                {
                    printf("Enter new value: ");
                    scanf("%d", &element);
                    arr[pos] = element;
                    printf("Element updated\n");
                }
                break;
            }

            case 6:
            {
                printf("Exiting program...\n");
                break;
            }

            default:
            {
                printf("Invalid choice! Try again.\n");
            }
        }

    } while(choice != 6);

    return 0;
}
