# 5972 택배 배송

import sys
input = sys.stdin.readline

import heapq

INF = 100_000_000

def dijkstra():
    weight[1] = 0

    heap = []
    heapq.heappush(heap, [0, 1])

    while heap:
        wgt, curr = heapq.heappop(heap)

        if wgt > weight[curr]:
            continue

        for next_, c in graph[curr]:
            cost = wgt + c
            if cost < weight[next_]:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

weight = [INF] * (N+1)

dijkstra()

print(weight[N])