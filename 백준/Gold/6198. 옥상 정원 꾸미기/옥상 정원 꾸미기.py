# 6198 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

N = int(input())
building = [int(input()) for _ in range(N)]

stack = []
total = 0
for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()

    total += len(stack)
    stack.append(building[i])

print(total)