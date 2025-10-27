# 1238 파티

import heapq

INF = 1_000_000_000

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n)) # 시작점에서의 가중치는 0
    weight[n] = 0

    while queue:
        wgt, now = heapq.heappop(queue) # 가중치와 현재 정점 정보 pop

        if weight[now] < wgt: # 현재 정점까지의 가중치와 지금까지의 가중치를 비교
            continue # 이미 작은 가중치(최단 거리)로 정점에 도착했을 경우 생략

        for v, w in graph[now]:
            cost = wgt + w

            if cost < weight[v]: 
                weight[v] = cost
                heapq.heappush(queue, (cost, v))

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])

res = [0] * (N+1)
for i in range(1, N+1):
    weight = [INF] * (N+1) # 해당 정점까지의 가중치(최단 거리) 저장
    dijkstra(i)
    res[i] += weight[X]

weight = [INF] * (N+1) # 해당 정점까지의 가중치(최단 거리) 저장
dijkstra(X)

result = []
for i in range(1, N+1):
    result.append(res[i] + weight[i])

print(max(result))