# 9461 파도반 수열

T = int(input())

for _ in range(T):
    N = int(input())

    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    dp[8] = 5
    dp[9] = 7
    dp[10] = 9
    dp[11] = 12
    dp[12] = 16

    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    print(dp[N])