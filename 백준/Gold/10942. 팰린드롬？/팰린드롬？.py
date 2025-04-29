# 10942 팰린드롬?

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N): # (1, 1), (3, 3) 등 한자리 수는 1
    dp[i][i] = 1

for j in range(N-1): # 두 자리의 경우, 두 문자가 같을 경우 1, 다를 경우 0
    if (lst[j] == lst[j+1]):
        dp[j][j+1] = 1
    else:
        dp[j][j+1] = 0

for cnt in range(N-2): # 세 자리에 경우, 양 끝이 같고 안에 문자가 1이면 1, 아니면 0
    for i in range(N-2-cnt):
        j = i + 2 + cnt
        if (lst[i] == lst[j]) and (dp[i+1][j-1] == 1):
            dp[i][j] = 1

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])