#include <stdio.h>
#define MAX 100

int main()
{
    int n, e;
    int graph[MAX][MAX] = {0};
    int indegree[MAX] = {0};
    int queue[MAX];
    int front = 0, rear = -1;
    int topoOrder[MAX];
    int count = 0;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of edges: ");
    scanf("%d", &e);

    printf("Enter edges (from to):\n");
    for (int i = 0; i < e; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u][v] = 1;
    }

    // Step 1: Compute indegree
    for (int v = 0; v < n; v++)
    {
        indegree[v] = 0;
        for (int u = 0; u < n; u++)
        {
            if (graph[u][v] == 1)
                indegree[v]++;
        }
    }

    // Step 2: Push indegree 0 vertices to queue
    for (int i = 0; i < n; i++)
    {
        if (indegree[i] == 0)
            queue[++rear] = i;
    }

    // Step 3: Kahn's Algorithm
    while (front <= rear)
    {
        int u = queue[front++];
        topoOrder[count++] = u;

        for (int v = 0; v < n; v++)
        {
            if (graph[u][v] == 1)
            {
                indegree[v]--;
                if (indegree[v] == 0)
                    queue[++rear] = v;
            }
        }
    }

    // Cycle detection
    if (count != n)
        printf("\nCycle detected! Topological sorting not possible.\n");
    else
    {
        printf("\nTopological Order: ");
        for (int i = 0; i < count; i++)
            printf("%d ", topoOrder[i]);
        printf("\n");
    }

    return 0;
}
