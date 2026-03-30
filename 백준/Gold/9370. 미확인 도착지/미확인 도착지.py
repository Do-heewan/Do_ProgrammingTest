# 9370 미확인 도착지

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
            cost = c + wgt
            if cost < weight[next_]:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])

for _ in range(int(input())):
    N, M, T = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])
        graph[b].append([a, cost])

    target = [int(input()) for _ in range(T)]

    weight = [INF] * (N+1)
    dijkstra(s) 

    distance = [-1] * (N+1)
    for t in target:
        distance[t] = weight[t]

    s_to_g = weight[g]
    s_to_h = weight[h]

    weight = [INF] * (N+1)
    dijkstra(g)

    distance_g = [-1] * (N+1)
    for t in target:
        distance_g[t] = s_to_g+weight[t]

    weight = [INF] * (N+1)
    dijkstra(h)

    distance_h = [-1] * (N+1)
    for t in target:
        distance_h[t] = s_to_h+weight[t]

    for i in range(1, N+1):
        if distance[i] == -1: continue

        elif distance[i] == distance_g[i] == distance_h[i]:
            print(i, end=' ')
    print()