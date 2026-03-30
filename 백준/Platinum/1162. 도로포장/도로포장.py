# 1162 도로포장

import sys
input = sys.stdin.readline

import heapq

INF = 10**18

def dijkstra():
    weight[1][0] = 0

    heap = []
    heapq.heappush(heap, [0, 1, 0])

    while heap:
        wgt, curr, k = heapq.heappop(heap)

        if wgt > weight[curr][k]:
            continue

        for next_, c in graph[curr]:
            cost = wgt + c

            if cost < weight[next_][k]:
                weight[next_][k] = cost
                heapq.heappush(heap, [cost, next_, k])

            if k < K and wgt < weight[next_][k+1]:
                weight[next_][k+1] = wgt
                heapq.heappush(heap, [wgt, next_, k+1])
            


N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

weight = [[INF] * (K+1) for _ in range(N+1)] # [j, k] => j로 가면서 K개의 도로를 포장

dijkstra()

print(min(weight[N]))