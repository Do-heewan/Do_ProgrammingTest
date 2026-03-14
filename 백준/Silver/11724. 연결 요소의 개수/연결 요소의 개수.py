# 11724 연결 요소의 개수

import sys
input = sys.stdin.readline

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = True

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not visited[ix]:
                Q.append(ix)
                visited[ix] = True

    return 1

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

res = 0
for i in range(1, N+1):
    if not visited[i]:
        res += bfs(i)

print(res)