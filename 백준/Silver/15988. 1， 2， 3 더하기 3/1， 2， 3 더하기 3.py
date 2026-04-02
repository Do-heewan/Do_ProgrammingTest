# 15988 1, 2, 3 더하기 3

T = int(input())

dp = [0] * (1_000_000+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1_000_001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009

for _ in range(T):
    N = int(input())
    print(dp[N] % 1_000_000_009)