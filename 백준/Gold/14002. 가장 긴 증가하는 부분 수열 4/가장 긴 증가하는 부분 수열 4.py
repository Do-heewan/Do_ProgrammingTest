# 14002 가장 긴 증가하는 부분 수열 4

N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N
route = [-1] * N

for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                route[i] = j
            # dp[i] = max(dp[i], dp[j]+1)

max_len = max(dp)
result = []
curr = dp.index(max_len)
while curr != -1:
    result.append(lst[curr])
    curr = route[curr]

print(len(result))
print(*result[::-1])