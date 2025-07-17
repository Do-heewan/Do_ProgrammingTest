# 1504 특정한 최단 경로

import heapq

INF = 1_000_000_000

def dijkstra(num, end):
    weight = [INF] * (N+1)

    queue = []
    heapq.heappush(queue, (0, num)) # 시작 위치의 가중치는 0

    weight[num] = 0

    while queue:
        wgt, now = heapq.heappop(queue) # 큐에 저장된 가중치와 정점 정보 pop

        if (weight[now] < wgt): # 현재 정점에 저장된 가중치가 더 작다 => 이미 작은 가중치로 현재 정점에 도착함
            continue

        for v, w in graph[now]:
            cost = wgt + w # 비용 = v로 가는데 드는 가중치 + 현재의 가중치
            if (cost < weight[v]): # 비용이 더 적게 들면
                weight[v] = cost # 더 작은 가중치로 변경
                heapq.heappush(queue, (cost, v)) # 힙에 푸쉬

    return weight[end]

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

v1, v2 = map(int, input().split())

result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

print(result if result < INF else -1)