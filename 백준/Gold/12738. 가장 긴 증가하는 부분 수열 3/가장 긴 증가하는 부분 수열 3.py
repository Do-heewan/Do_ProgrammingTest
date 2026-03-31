# 12015 가장 긴 증가하는 부분 수열 3

import sys
input = sys.stdin.readline

import bisect

N = int(input())
lst = list(map(int, input().split()))

dp = []

for x in lst:
    idx = bisect.bisect_left(dp, x)

    if idx == len(dp):
        dp.append(x)
    else:
        dp[idx] = x

print(len(dp))