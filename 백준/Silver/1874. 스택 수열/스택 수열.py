# 1874 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
seq = list(int(input()) for _ in range(N))

nums = [i for i in range(1, N+1)]
result = []

stack = []
idx = 0

result = []
for i in range(1, N+1):
    stack.append(i)
    result.append("+")

    while idx < N and stack[-1] == seq[idx]:
        stack.pop()
        idx += 1
        result.append("-")
        if not stack:
            break

if stack:
    print("NO")
else:
    for r in result:
        print(r)