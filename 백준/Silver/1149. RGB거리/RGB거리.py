# 1149 RGB 거리

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i-1][2]

print(min(dp[N]))