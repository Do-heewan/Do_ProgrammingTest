N = int(input())
lst = [0] + list(map(int, input().split()))

action = [1, 2, 3]
dp = [0] * (N+1)
dp[1] = lst[1]
dp[2] = lst[2]
dp[3] = lst[3]

for i in range(4, N+1):
	dp[i] = min(dp[i-3] + lst[i], dp[i-2] + lst[i], dp[i-1] + lst[i])


print(min(dp[N-2], dp[N-1], dp[N]))