# 17175 피보나치는 지겨웡~

import sys
input = sys.stdin.readline

dp = [0] * (51)
dp[0] = 1
dp[1] = 1

for i in range(2, 51):
    dp[i] = dp[i-2] + dp[i-1] + 1

print(dp[int(input())] % 1_000_000_007)