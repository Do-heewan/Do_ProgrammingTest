# 1967 트리의 지름

import sys
input = sys.stdin.readline

INF = 1_000_000_000

import heapq

def dijkstra(n):
    weight[n] = 0

    heap = []
    heapq.heappush(heap, [0, n])

    while heap:
        wgt, curr = heapq.heappop(heap)

        if wgt > weight[curr]:
            continue

        for next_, c in graph[curr]:
            cost = c + wgt
            if cost < weight[next_]:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

weight = [INF] * (N+1)
dijkstra(1)

max_distance = 0
far_node = 0
for idx, wgt in enumerate(weight[1:]):
    if wgt > max_distance:
        far_node = idx+1
        max_distance = wgt

weight = [INF] * (N+1)
dijkstra(far_node)

max_distance = 0
for wgt in weight:
    if wgt == INF: continue
    max_distance = max(max_distance, wgt)

print(max_distance)