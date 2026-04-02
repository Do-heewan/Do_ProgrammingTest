# 16194 카드 구매하기 2

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [100_001] * (N+1)

for i in range(1, N+1):
    dp[i] = lst[i]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+lst[j])

print(dp[N])