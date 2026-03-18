# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    Q = deque()
    Q.append(1)
    visited[1] = True

    while Q:
        curr = Q.popleft()

        for ix in graph[curr]:
            if not visited[ix]:
                Q.append(ix)
                visited[ix] = True
                res[ix] = curr

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

res = {0:0, 1:0}

bfs()

for i in list(sorted(res))[2:]:
    print(res[i])