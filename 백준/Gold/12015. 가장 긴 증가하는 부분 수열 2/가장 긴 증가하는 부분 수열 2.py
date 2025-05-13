# 12015 가장 긴 증가하는 부분 수열 2

import sys
from bisect import bisect_left
input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]

for ix in seq:
    if (dp[-1] < ix):
        dp.append(ix)
    else:
        idx = bisect_left(dp, ix)
        dp[idx] = ix

print(len(dp))