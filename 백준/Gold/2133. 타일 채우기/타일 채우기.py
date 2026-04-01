# 2133 타일 채우기

N = int(input())

if N % 2 != 0:
    print(0)

else:
    dp = [0] * (N+1)
    dp[2] = 3

    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2
    
    print(dp[N])