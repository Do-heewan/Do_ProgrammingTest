#include<stdio.h>
int main()
{
    int a;
    scanf("%d", &a);
    int b = a;
    
    int i = 0;
    while (true)
    {
        a = (a%10)*10 + ((a/10) + (a%10))%10;
        i++;
        
        if (a == b)
        {
            printf("%d", i);
            break;
        }
    }
    return 0;
}