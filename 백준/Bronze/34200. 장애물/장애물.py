# 34200 장애물

INF = 1_000_000

N = int(input())
wall = set(map(int, input().split()))

max_height = max(wall)
dp = [INF for _ in range(max_height+2)]

dp[0] = 0
for i in range(1, max_height+2):
    if i in wall:
        continue
    dp[i] = min(dp[i-2] + 1, dp[i-1] + 1, dp[i])

print(dp[max_height+1] if dp[max_height+1] != INF else -1)