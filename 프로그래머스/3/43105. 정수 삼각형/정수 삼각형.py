def solution(triangle):
    L = len(triangle)
    dp = [[0] * i for i in range(1, L+1)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]
    
    for i in range(2, L):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]) 
        dp[i][i] = dp[i-1][-1] + triangle[i][-1]
            
    return max(dp[-1])