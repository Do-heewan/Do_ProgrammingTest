# 12865 평범한 배낭

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# dp = [0] * (K+1)
# dp[0] = 0

# for w, v in items:
#     for i in range(K, w-1, -1):
#         dp[i] = max(dp[i], dp[i-w]+v)

# print(max(dp))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = items[i-1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])