#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    

    int min = 1000000;
    int max = -1000000;
    
    for (int i=0; i < n; i++)
    {
        int n[i];
        scanf("%d", &n[i]);
        
        if (n[i] < min)
        {
            min = n[i];
        }
        
        if (n[i] > max)
        {
            max = n[i];
        }
    }
    
    printf("%d %d", min, max);
    return 0;
}