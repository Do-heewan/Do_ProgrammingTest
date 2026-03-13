# 2342 Dance Dance Revolution

import sys
input = sys.stdin.readline

def cost(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a-b) == 2:
        return 4
    return 3

arr = list(map(int, input().split()))
arr.pop()

INF = 10**9
n = len(arr)

dp = [[[INF]*5 for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    next = arr[i]

    for l in range(5):
        for r in range(5):

            cur = dp[i][l][r]
            if cur == INF:
                continue

            # 왼발 이동
            dp[i+1][next][r] = min(
                dp[i+1][next][r],
                cur + cost(l, next)
            )

            # 오른발 이동
            dp[i+1][l][next] = min(
                dp[i+1][l][next],
                cur + cost(r, next)
            )


ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[n][l][r])

print(ans)