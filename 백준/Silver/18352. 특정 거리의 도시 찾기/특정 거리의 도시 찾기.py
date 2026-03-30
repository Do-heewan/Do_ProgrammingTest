# 18352 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = 0

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if visited[ix] == -1:
                visited[ix] = visited[c]+1
                Q.append(ix)


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (N+1)

bfs(X)

result = []
for i in range(1, N+1):
    if visited[i] == K:
        result.append(i)

if result:
    for r in result:
        print(r)
else:
    print(-1)