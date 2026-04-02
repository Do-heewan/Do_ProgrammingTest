# 2302 극장 좌석

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
fix = [int(input()) for _ in range(M)]

dp = [[0, 0] for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 0

for f in fix:
    dp[f][1] = -1

for i in range(2, N+1):
    if dp[i][1] == -1:
        if dp[i-1][1] != -1:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0]

    else:
        if dp[i-1][1] != -1:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = 0

if dp[N][1] != -1:
    print(sum(dp[N]))
else:
    print(dp[N][0])