# 11725 트리의 부모 찾기

import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = [[] for _ in range(N+1)]

def dfs(num):
    visited[num] = True

    for ix in graph[num]:
        if not (result[ix]):
            result[ix].append(num)

        if not visited[ix]:
            dfs(ix)

dfs(1)
for i in range(2, len(result)):
    print(*result[i])