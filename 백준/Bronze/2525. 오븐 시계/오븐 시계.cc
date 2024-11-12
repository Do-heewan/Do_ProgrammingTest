#include <stdio.h>
int main ()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    if (b+c < 60)
    {
        printf("%d %d", a, b+c);
    }
    
    else if (b+c >= 60)
    {
        a = a+(b+c)/60;
        
        if (a < 24)
        {
            printf("%d %d", a, (b+c)%60);
        }
           
        else if (a >= 24)
        {
            printf("%d %d", a-24, (b+c)%60);
        }
    }
    
    return 0;
}