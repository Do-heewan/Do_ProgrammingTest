# 9461 파도반 수열

T = int(input())

for _ in range(T):
    N = int(input())

    dp = [1] * 101
    dp[4] = 2
    dp[5] = 2

    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N])