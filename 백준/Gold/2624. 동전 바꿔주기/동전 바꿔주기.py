# 2624 동전 바꿔주기

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (k+1) for _ in range(T+1)]
dp[0][0] = 1

for i in range(1, k+1):
    curr_coin, cnt = coins[i-1]

    for money in range(T+1):
        for j in range(cnt+1):
            if money - curr_coin*j >= 0:
                dp[money][i] += dp[money-curr_coin*j][i-1]

print(dp[T][k])