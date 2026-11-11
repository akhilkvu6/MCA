#include<stdio.h>

#define MAX 100
int top=-1; // Global top index
int stack[MAX]; // Global stack array

void push(int n)
{
    if(top>=MAX-1)
    {
        printf("stack overflow");
        return;
    }
    else
    {
        stack[++top]=n;

    }
}

int pop()
{
    if(top<0)
    {
        printf("stack underflow");
        return -1;
    }
    else
    {
        return stack[top--];
    }
}

void DFS(int adjMatrix[MAX][MAX], int n, int start) 
{
    int visited[MAX] = {0};

    push(start);
    visited[start] = 1;

    printf("DFS traversal starting from node %d: ", start);

    while (top != -1) 
    { 
        int node = pop();
        printf("%d ", node);

        
        for (int i = 0; i < n; i++) 
        {
            if (adjMatrix[node][i] == 1 && visited[i]==0) 
            {
                push(i);
                visited[i] = 1;
            
            }
        }
    }
    printf("\n");
}

int main() 
{
    int n, start;
    int adjMatrix[MAX][MAX];

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {    
            scanf("%d", &adjMatrix[i][j]);
        }
    }

    printf("Enter starting node: ");
    scanf("%d", &start);

    DFS(adjMatrix, n, start);

    return 0;
}