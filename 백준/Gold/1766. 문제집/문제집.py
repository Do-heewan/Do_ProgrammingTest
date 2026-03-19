# 1766 문제집

import heapq
from collections import deque

def topo_sort():
    Q = []
    result = []

    for i in range(1, N+1):
        if degree[i] == 0:
            heapq.heappush(Q, i)
    
    while Q:
        curr = heapq.heappop(Q)
        result.append(curr)

        for ix in graph[curr]:
            degree[ix] -= 1

            if degree[ix] == 0:
                heapq.heappush(Q, ix)

    print(*result)

N, M = map(int, input().split())

degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

topo_sort()