# 18352 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    visited[n] = True
    Q = deque()
    Q.append(n)

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not visited[ix]:
                visited[ix] = True
                distance[ix] = distance[c] + 1
                Q.append(ix)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False for _ in range(N+1)]
distance = [0 for _ in range(N+1)]
bfs(X)

if K in distance:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
else:
    print(-1)