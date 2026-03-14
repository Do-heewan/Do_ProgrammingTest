# 1753 최단 경로

import sys
input = sys.stdin.readline

import heapq

INF = 10_000_000

def dijkstra(n):
    heap = []
    weight[n] = 0

    heapq.heappush(heap, (0, n))

    while heap:
        wgt, curr = heapq.heappop(heap)

        if wgt > weight[curr]:
            continue

        for next, cost in graph[curr]:
            if weight[next] > wgt + cost:
                weight[next] = wgt + cost
                heapq.heappush(heap, (wgt+cost, next))

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

weight = [INF] * (V+1)

dijkstra(K)

for w in weight[1:]:
    if w == INF:
        print("INF")
    else:
        print(w)