# 2670 연속부분최대곱

N = int(input())
lst = [float(input()) for _ in range(N)]

dp = [0] * N
dp[0] = lst[0]

for i in range(1, N):
    dp[i] = max(lst[i], dp[i-1]*lst[i])

print(f"{max(dp):.3f}")