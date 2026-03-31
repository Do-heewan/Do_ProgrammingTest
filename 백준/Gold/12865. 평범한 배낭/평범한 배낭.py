# 12865 평범한 배낭

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 0

for w, v in items:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

print(max(dp))