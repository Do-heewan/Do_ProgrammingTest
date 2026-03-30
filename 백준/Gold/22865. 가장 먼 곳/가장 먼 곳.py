# 22865 가장 먼 곳

import sys
input = sys.stdin.readline

import heapq

INF = 1_000_000_000

def dijkstra():
    heap = []

    for p in [A, B, C]:
        weight[p] = 0
        heapq.heappush(heap, [0, p])

    while heap:
        wgt, curr = heapq.heappop(heap)

        if wgt > weight[curr]:
            continue

        for next_, c in graph[curr]:
            cost = c + wgt
            if weight[next_] > cost:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

N = int(input())
A, B, C = map(int, input().split())
people = [A, B, C]

M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

weight = [INF] * (N+1)

dijkstra()

max_distance = -1
answer = 0
for i in range(1, N+1):
    if i in people:
        continue

    if weight[i] > max_distance:
        answer = i
        max_distance = weight[i]

print(answer)