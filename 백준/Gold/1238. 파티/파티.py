# 1238 파티

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
            if weight[next_] > cost:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

result = [0] * (N+1)
for i in range(1, N+1):
    weight = [INF] * (N+1)
    dijkstra(i)
    
    if i == X:
        for k in range(1, N+1):
            if k == X:
                continue
            result[k] += weight[k]
            continue

    result[i] += weight[X]

print(max(result))