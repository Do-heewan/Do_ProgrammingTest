# # 12015 가장 긴 증가하는 부분 수열 2

import sys
input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]

for ix in seq:
    if (dp[-1] < ix):
        dp.append(ix)

    else:
        start, end = 0, len(dp)-1
        while (start < end):
            mid = (start + end) // 2

            if (ix > dp[mid]):
                start = mid + 1

            else:
                end = mid
        dp[end] = ix

print(len(dp))