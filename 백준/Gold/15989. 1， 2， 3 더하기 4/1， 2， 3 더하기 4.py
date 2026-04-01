# 15989 1, 2, 3 더하기 4

T = int(input())

for _ in range(T):
    N = int(input())
    
    dp = [1] * (N+1)

    for i in range(2, N+1):
        dp[i] += dp[i-2]
    
    for i in range(3, N+1):
        dp[i] += dp[i-3]

    print(dp[N])