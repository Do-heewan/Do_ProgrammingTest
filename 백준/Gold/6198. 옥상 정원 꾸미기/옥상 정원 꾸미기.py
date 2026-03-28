# 6198 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
cnt = 0

for i in range(N):
    while stack and nums[stack[-1]] <= nums[i]:
        stack.pop()
    
    cnt += len(stack)
    stack.append(i)

print(cnt)