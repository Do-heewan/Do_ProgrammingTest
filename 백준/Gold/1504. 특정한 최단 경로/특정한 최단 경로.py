# 1504 특정한 최단 경로

import sys
input = sys.stdin.readline

import heapq

INF = 100_000_000

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

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

target_a, target_b = map(int, input().split())

weight = [INF] * (N+1)
dijkstra(1)
one_to_a = weight[target_a]
one_to_b = weight[target_b]

weight = [INF] * (N+1)
dijkstra(target_a)
a_to_b = weight[target_b]
a_to_end = weight[N]

weight = [INF] * (N+1)
dijkstra(target_b)
b_to_end = weight[N]
b_to_a = weight[target_a]

if one_to_a == INF or a_to_b == INF or b_to_end == INF:
    print(-1)
else:
    print(min(one_to_a+a_to_b+b_to_end, one_to_b+b_to_a+a_to_end))