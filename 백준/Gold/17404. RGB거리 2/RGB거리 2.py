# 17404 RGB 거리 2

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

answer = 100_000_000
for start in range(3):
    dp = [[100_000_000] * 3 for _ in range(N+1)]
    dp[1][start] = lst[0][start]
    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lst[i-1][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lst[i-1][2]

    dp[N][start] = 100_000_000
    answer = min(answer, min(dp[N]))

print(answer)