
#include <stdio.h>
int main ()
{
    int a, max = 0;
    
    for (int i=0; i < 9; i++)
    {
        int n[i];
        scanf("%d", &n[i]);
        
        if (n[i] > max) 
        {
            max = n[i]; 
            a=i;
        }
    }
    
    printf("%d\n", max);
    printf("%d", a+1);
    return 0;
}