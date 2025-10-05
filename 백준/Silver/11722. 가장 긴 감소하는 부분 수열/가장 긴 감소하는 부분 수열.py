# 11722 가장 긴 감소하는 부분 수열

N = int(input())
lst = list(map(int, input().split()))

rev_lst = lst[::-1]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if rev_lst[i] > rev_lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))