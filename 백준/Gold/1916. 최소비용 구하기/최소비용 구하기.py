# 1916 최소비용 구하기

import sys
input = sys.stdin.readline

import heapq

INF = 10 ** 8

def dijkstra(n):
    heap = []
    weight[n] = 0

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
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())

weight = [INF] * (N+1)

dijkstra(start)

print(weight[end])