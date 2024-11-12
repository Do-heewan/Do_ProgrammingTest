#include<stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    
    int n1 = b%10;
    int n2 = b/10%10;
    int n3 = b/100;
    
    printf("%d\n", a*n1);
    printf("%d\n", a*n2);
    printf("%d\n", a*n3);
    printf("%d", a*n1 + 10*a*n2 + 100*a*n3);
    
    return 0;
}