# 1932 정수 삼각형

N = int(input())
lst = [0] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]
dp[1][0] = lst[1][0]

for i in range(2, N+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i-1][j] + lst[i][j]
        elif j == i-1:
            dp[i][j] = dp[i-1][j-1] + lst[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + lst[i][j]

print(max(dp[N]))