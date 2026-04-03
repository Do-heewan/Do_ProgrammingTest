# 15681 트리와 쿼리

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def dfs(n):
    visited[n] = True

    for ix in graph[n]:
        if not visited[ix]:
            degree[n] += dfs(ix)

    return degree[n]

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = [int(input()) for _ in range(Q)]

visited = [False] * (N+1)
degree = [1] * (N+1)

dfs(R)

for s in start:
    print(degree[s])