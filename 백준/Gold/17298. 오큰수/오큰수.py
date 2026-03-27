# 17298 오큰수

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stack = []
result = [-1] * N

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        result[idx] = nums[i] 

    stack.append(i)

print(*result)