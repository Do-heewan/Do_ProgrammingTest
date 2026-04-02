# 1912 연속합

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [-1001] * (N+1)

for i in range(1, N+1):
    dp[i] = max(lst[i], dp[i-1]+lst[i])

print(max(dp))