# 2470 두 용액

import sys
input = sys.stdin.readline

INF = 10_000_000_000

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

left = 0
right = N-1

answer = (0, 0)
min_value = INF

while left < right:
    curr = lst[left] + lst[right]
    abs_curr = abs(curr)

    if abs_curr < min_value:
        min_value = abs_curr
        answer = (lst[left], lst[right])

    if curr < 0:
        left += 1
    else:
        right -= 1

print(*answer)