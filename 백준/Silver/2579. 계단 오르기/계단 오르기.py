# 2579 계단 오르기

N = int(input())
stair = [0] + [int(input()) for _ in range(N)]

dp = [[0] * 2 for _ in range(N+1)]
dp[1][0] = stair[1]

for i in range(2, N+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1])+stair[i]
    dp[i][1] = dp[i-1][0]+stair[i]

print(max(dp[N]))