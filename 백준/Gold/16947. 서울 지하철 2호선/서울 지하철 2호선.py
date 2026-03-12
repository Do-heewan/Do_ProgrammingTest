# 16947 서울 지하철 2호선

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def find_cycle():
    Q = deque()
    for i in range(1, N+1):
        if degree[i] == 1:
            Q.append(i)

    while Q:
        curr = Q.popleft()
        cycle[curr] = False

        for next in graph[curr]:
            degree[next] -= 1
            if degree[next] == 1:
                Q.append(next)

def bfs():
    Q = deque()
    for i in range(1, N+1):
        if cycle[i]:
            Q.append(i)
            visited[i] = 0

    while Q:
        curr = Q.popleft()

        for ix in graph[curr]:
            if visited[ix] == -1:
                visited[ix] = visited[curr]+1
                Q.append(ix)

N = int(input())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

cycle = [True] * (N+1)
find_cycle()

visited = [-1] * (N+1)
bfs()

for v in visited[1:]:
    print(v, end=' ')