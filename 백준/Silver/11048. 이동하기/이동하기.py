# 11048 이동하기

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j]+lst[i-1][j-1], dp[i][j-1]+lst[i-1][j-1])

print(dp[N][M])