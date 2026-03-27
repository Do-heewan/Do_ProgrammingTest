# 10828 스택

import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    cmd = list(input().split())

    if cmd[0] == "push":
        num = cmd[1]
        stack.append(num)

    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        print(0 if stack else 1)

    elif cmd[0] == "pop":
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)