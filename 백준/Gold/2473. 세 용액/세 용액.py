# 2473 세 용액

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 10 ** 15
result = [0, 0, 0]

for i in range(N-2):
    left = i+1
    right = N-1

    while left < right:
        curr = lst[i] + lst[left] + lst[right]

        if abs(curr) < abs(answer):
            answer = curr
            result = [lst[i], lst[left], lst[right]]

        if curr > 0:
            right -= 1
        else:
            left += 1

print(*result)