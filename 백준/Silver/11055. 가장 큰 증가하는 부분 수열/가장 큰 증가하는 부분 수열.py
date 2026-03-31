# 11055 가장 큰 증가하는 부분 수열

N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N
dp[0] = lst[0]

for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+lst[i])
        else:
            dp[i] = max(dp[i], lst[i])

print(max(dp))