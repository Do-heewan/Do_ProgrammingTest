# 2293 동전 1

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

# dp[i] => i원을 만드는 경우의 수
dp = [0] * (K+1)
dp[0] = 1
for c in coin:
    for i in range(c, K+1):
        dp[i] += dp[i-c]

print(dp[K])