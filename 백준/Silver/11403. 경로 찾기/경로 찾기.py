# 11403 경로 찾기

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            graph[i].append(j)

for i in range(N):
    visited = [0] * N

    Q = deque()
    Q.append(i)
    
    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not visited[ix]:
                visited[ix] = 1
                Q.append(ix)

    print(*visited)