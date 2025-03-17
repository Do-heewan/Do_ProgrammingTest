# 1753 최단 경로

import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())

start = int(input())

INF = 1_000_000_000
graph = [[] for _ in range(V+1)]
weight = [INF] * (V+1)

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(num):
    queue = []
    heapq.heappush(queue, (0, num))
    weight[num] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if (weight[now] < dist):
            continue

        for v, w in graph[now]:
            cost = dist + w
            if (cost < weight[v]):
                weight[v] = cost
                heapq.heappush(queue, (cost, v))

dijkstra(start)

for i in range(1, len(weight)):
    if (weight[i] == INF):
        print("INF")

    else:
        print(weight[i])