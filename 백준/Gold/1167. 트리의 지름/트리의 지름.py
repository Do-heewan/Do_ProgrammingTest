# 1167 트리의 지름

import sys
input = sys.stdin.readline

import heapq

INF = 10 ** 15

def dijkstra(n):
    weight[n] = 0

    heap = []
    heapq.heappush(heap, [0, n])

    while heap:
        wgt, curr = heapq.heappop(heap)

        if wgt > weight[curr]:
            continue

        for next_, c in graph[curr]:
            cost = wgt + c
            if cost < weight[next_]:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N):
    ipt = list(map(int, input().split()))
    
    node = ipt[0]
    for i in range(1, len(ipt), 2):
        if ipt[i] == -1:
            continue
        
        graph[node].append([ipt[i], ipt[i+1]])

weight = [INF] * (N+1)
dijkstra(1)

far_node = -1
max_distance = 0

for i, d in enumerate(weight[1:]):
    if d > max_distance:
        max_distance = d
        far_node = i+1

weight = [INF] * (N+1)
dijkstra(far_node)

for d in weight[1:]:
    max_distance = max(max_distance, d)

print(max_distance)