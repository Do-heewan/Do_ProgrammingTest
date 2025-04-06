# 9465 스티커

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(2)]

    res = []
    for _ in range(2):
        res.append(list(map(int, input().split())))

    # 스티커 길이가 1일 경우
    dp[0][0] = res[0][0]
    dp[1][0] = res[1][0]

    if (N == 1):
        print(max(dp[0][0], dp[1][0]))
        continue

    # 스티커 길이가 2일 경우
    dp[0][1] = res[1][0] + res[0][1]
    dp[1][1] = res[0][0] + res[1][1]

    if (N == 2):
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3 이상일 경우
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + res[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + res[1][i]

    print(max(dp[0][N-1], dp[1][N-1]))