# 1260 DFS와 BFS

from collections import deque
import sys

input = sys.stdin.readline

def bfs(n):
    b_visited[n] = True
    Q = deque()
    Q.append(n)
    print(n, end=' ')

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not b_visited[ix]:
                Q.append(ix)
                b_visited[ix] = True
                print(ix, end=' ')

def dfs(n):
    d_visited[n] = True
    print(n, end=' ')

    for ix in graph[n]:
        if not d_visited[ix]:
            dfs(ix)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

b_visited = [False] * (N+1)
d_visited = [False] * (N+1)

dfs(V)
print()
bfs(V)