# 10845 큐

import sys

input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    cmd = input().strip().split()

    if (len(cmd) == 2):
        op, x = cmd[0], cmd[1]

        if (op == "push"):
            li.append(x)

    if (cmd[0] == "pop"):
        if (len(li) == 0):
            print(-1)
        else:
            print(li[0])
            del li[0]

    elif (cmd[0] == "size"):
        print(len(li))

    elif (cmd[0] == "empty"):
        if (len(li) == 0):
            print(1)
        else:
            print(0)

    elif (cmd[0] == "front"):
        if (len(li) == 0):
            print(-1)
        else:
            print(li[0])

    elif (cmd[0] == "back"):
        if (len(li) == 0):
            print(-1)
        else:
            print(li[-1])
