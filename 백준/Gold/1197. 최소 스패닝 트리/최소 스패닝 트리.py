# 1197 최소 스패닝 트리 (Prim)

import sys
input = sys.stdin.readline

import heapq

INF = 100_000_000

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

visited = set()

heap = []
heapq.heappush(heap, [0, 1])

answer = 0
while heap:
    wgt, curr = heapq.heappop(heap)

    if curr in visited:
        continue

    visited.add(curr)
    answer += wgt

    for next_, c in graph[curr]:
        if next_ not in visited:
            heapq.heappush(heap, [c, next_])

print(answer)