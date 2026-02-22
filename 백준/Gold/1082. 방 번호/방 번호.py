# 1082 방 번호

N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [-1] * 51
for i in range(N):
    dp[P[i]] = i

for i in range(1, M+1):
    for j in range(1, i):
        if dp[j] != -1:
            dp[i] = max(dp[i], int(str(dp[i-j]) + str(dp[j])))

print(max(dp[:M+1]))