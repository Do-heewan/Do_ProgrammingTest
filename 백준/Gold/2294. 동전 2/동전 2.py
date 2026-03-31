# 동전 2

INF = 100_000

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [INF] * (100000+1)
dp[0] = 0

for c in coins:
    dp[c] = 1
    for i in range(c, K+1):
        dp[i] = min(dp[i], dp[i-c]+1)

print(dp[K] if dp[K] != INF else -1)