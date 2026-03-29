import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
    cmd = list(input().split())

    if cmd[0] == "push":
        num = cmd[1]
        queue.append(num)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        print(0 if queue else 1)

    elif cmd[0] == "pop":
        if queue:
            a = queue.popleft()
            print(a)
        else:
            print(-1)

    elif cmd[0] == "front":
        print(queue[0] if queue else -1)

    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)