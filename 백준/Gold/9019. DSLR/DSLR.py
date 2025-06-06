# 9019 DSLR

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(start, end):
    Q = deque()
    Q.append([start, ''])
    visited = [False] * 10001
    visited[start] = True

    while Q:
        num, command = Q.popleft()

        if (num == end):
            return command
        
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            Q.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            Q.append([s, command + 'S'])

        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            visited[l] = True
            Q.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            Q.append([r, command + 'R'])

for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))