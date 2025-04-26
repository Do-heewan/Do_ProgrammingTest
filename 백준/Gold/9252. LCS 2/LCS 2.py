# 9252 LCS 2

import sys
input = sys.stdin.readline

first = [''] + list(input().rstrip())
second = [''] + list(input().rstrip())

dp = [['' for _ in range(len(second))] for _ in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + first[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

result = dp[-1][-1]
print(len(result), result, sep="\n")