# 1351 무한 수열

N, P, Q = map(int, input().split())

dp = {}
dp[0] = 1

def seq(num):
    if (num in dp):
        return dp[num]
    
    else:
        dp[num] = seq(num // P) + seq(num // Q)
        return dp[num]

print(seq(N))