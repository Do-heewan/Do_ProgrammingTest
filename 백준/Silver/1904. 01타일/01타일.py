# 1904 01타일

N = int(input())

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N] % 15746)