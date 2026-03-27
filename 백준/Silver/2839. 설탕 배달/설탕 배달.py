# 2839 설탕 배달

import sys
input = sys.stdin.readline

INF = 5000

N = int(input())

dp = [INF] * (5000+1)
dp[3] = 1
dp[5] = 1

for i in range(1, N+1):
    dp[i] = min(dp[i], dp[i-5]+1, dp[i-3]+1)

print(dp[N] if dp[N] != INF else -1)