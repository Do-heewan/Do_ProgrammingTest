#include <stdio.h>
int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    int score;
    if ( a == b && b == c)
    {
        score = 10000 + a*1000;
        printf("%d", score);
    }
    
    else if (a == b)
    {
        score = 1000 + a*100;
        printf("%d", score);
    }
    
    else if (b == c)
    {
        score = 1000 + b*100;
        printf("%d", score);
    }
    
    else if (c == a)
    {
        score = 1000 + c*100;
        printf("%d", score);
    }
    
    else
    {
        if (a > b && a > c)
        {
            score = a*100;
            printf("%d", score);
        }
        
        else if (b > c)
        {
            score = b*100;
            printf("%d", score);
        }
        
        else
        {
            score = c*100;
            printf("%d", score);
        }
    }
    return 0;

}