# 2225 합분해

MOD = 1_000_000_000

N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]

dp = [[0] * (K+1) for _ in range(N+1)] # dp[n][k] k개의 수로 n을 만드는 경우의 수
dp[0][0] = 1 # 0을 0개로 만드는 경우의 수는 1

for n in range(N+1):
    for k in range(1, K+1):
        dp[n][k] = dp[n-1][k] + dp[n][k-1]

print(dp[N][K] % MOD)