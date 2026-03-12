#include<stdio.h>
int main()
{
    int x, n , a, b; //x : 총금액 // n : 물건의 종류의 수 // a : 각 물건의 가격 // b : 각 물건을 산 갯수
    scanf("%d", &x);
    scanf("%d", &n);
    
    for (int i = 0; i < n; i ++)
    {
        scanf("%d %d", &a, &b);
        x = x - (a * b);
    }
    
    if (x == 0)
        printf("Yes");
    else
        printf("No");
    
    return 0;
}