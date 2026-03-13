# 2606 바이러스

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

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

bfs(1)

print(sum(visited)-1)