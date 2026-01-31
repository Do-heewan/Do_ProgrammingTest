# 16562 친구비

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = True

    lst = [n]
    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if not visited[ix]:
                visited[ix] = True
                Q.append(ix)
                lst.append(ix)

    return lst


N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

visited = [False] * (N+1)

res = []
for i in range(1, N+1):
    if not visited[i]:
        res.append(bfs(i))

costs = 0
for r in res:
    cost = 10_000_001
    for ix in r:
        cost = min(cost, A[ix])
    costs += cost

print(costs if costs <= K else "Oh no")