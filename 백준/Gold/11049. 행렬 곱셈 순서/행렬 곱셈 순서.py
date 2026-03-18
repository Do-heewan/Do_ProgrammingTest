# 11049 행렬 곱셈 순서

import sys
input = sys.stdin.readline

INF = 2**31

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))

dp = [[INF] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for i in range(1, N):
    for j in range(N-i):
        for k in range(j, j+i):
            temp = dp[j][k] + dp[k+1][j+i] + (matrix[j][0] * matrix[k][1] * matrix[j+i][1])
            dp[j][j+i] = min(dp[j][j+i], temp)

print(dp[0][N-1])