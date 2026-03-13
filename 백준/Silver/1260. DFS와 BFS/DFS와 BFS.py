# 1260 DFS와 BFS

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = True
    print(n, end=' ')

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not visited[ix]:
                print(ix, end=' ')
                Q.append(ix)
                visited[ix] = True

def dfs(n):
    visited[n] = True
    print(n, end=' ')

    for ix in graph[n]:
        if not visited[ix]:
            dfs(ix)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [False] * (N+1)
dfs(V)

print()

visited = [False] * (N+1)
bfs(V)