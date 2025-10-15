# 14938 서강 그라운드

import heapq

INF = 1_000_000_000

def dijkstra(n, m):
    queue = []
    heapq.heappush(queue, (0, n))
    weighted = [INF] * (N+1)
    weighted[n] = 0

    while queue:
        wgt, now = heapq.heappop(queue)

        if (weighted[now] < wgt): # 현재 정점에 저장된 가중치가 더 작다 => 이미 작은 가중치로 현재 정점에 도착함
            continue

        for v, w in graph[now]:
            cost = wgt + w
            if cost <= m:
                weighted[v] = cost
                heapq.heappush(queue, (cost, v))
                # print(f"{now} -> {v}, {cost} // {result}")

    result = 0
    for i in range(1, N+1):
        if weighted[i] <= M:
            result += item[i]

    return result

N, M, R = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

ans = 0
for i in range(1, N+1):
    ans = max(ans, dijkstra(i, M))

print(ans)