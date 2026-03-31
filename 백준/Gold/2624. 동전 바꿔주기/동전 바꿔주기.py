# 2624 동전 바꿔주기

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (T+1)
dp[0] = 1

for c, cnt in coins:
    for money in range(T, 0, -1):
        for i in range(1, cnt+1):
            if money - c * i >= 0:
                dp[money] += dp[money-c*i]

print(dp[T])