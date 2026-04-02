# 2156 포도주 시식

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

dp = [[0] * 2 for _ in range(N+1)]
dp[1][0] = lst[1]

for i in range(2, N+1):
    dp[i][0] = max(dp[i-2][0] + lst[i], dp[i-2][1] + lst[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + lst[i])

print(max(dp[N]))