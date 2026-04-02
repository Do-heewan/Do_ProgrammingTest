# 2565 전깃줄

N = int(input())
lane = [list(map(int, input().split())) for _ in range(N)]
lane.sort()

dp = [1] * N

for i in range(N):
    for j in range(i):
        if lane[i][1] > lane[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))