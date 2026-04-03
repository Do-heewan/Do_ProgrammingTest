# 11066 파일 합치기

T = int(input())

for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    # 1. 누적합 구하기
    prefix = [0] * (N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + lst[i]

    dp = [[0] * (N+1) for _ in range(N+1)]
    # 2. length를 기준으로
    for length in range(2, N+1):
        for i in range(1, N-length+2):
            j = i + length - 1
            dp[i][j] = 100_000_000

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix[j] - prefix[i-1])
                dp[i][j] = min(cost, dp[i][j])

    print(dp[1][N])