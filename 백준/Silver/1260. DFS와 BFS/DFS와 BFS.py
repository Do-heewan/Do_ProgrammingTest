# 1260 DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    print(v, end = " ")
    visited_dfs[v] = True

    for ix in graph[v]:
        if not (visited_dfs[ix]):
            dfs(ix)

def bfs(v):
    print(v, end = " ")
    visited_bfs[v] = True
    Q = deque([v])

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not (visited_bfs[ix]):
                visited_bfs[ix] = True
                print(ix, end = " ")
                Q.append(ix)

dfs(V)
print()
bfs(V)