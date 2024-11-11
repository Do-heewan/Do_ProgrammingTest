#include<stdio.h>
int main()
{
    int N;
    scanf("%d", &N);
    
    for(int row = 1; row <= N; row++) 
    {

	for(int i = 0; i < N - row; i++) 
    {
		printf(" ");
	}

	for(int j = 0; j < row; j++) 
    {
		printf("*");
	}
 
	printf("\n");
    }
    return 0;
}