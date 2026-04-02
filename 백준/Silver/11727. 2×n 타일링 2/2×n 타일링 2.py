# 11727 2xn 타일링 2

N = int(input())

dp = [0] * (1000+1)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007

print(dp[N] % 10007)