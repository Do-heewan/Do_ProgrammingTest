# 1916 최소 비용 구하기

import heapq

N = int(input())
M = int(input())

INF = 100_000_000
graph = [[] for _ in range(N+1)]
weight = [INF] * (N+1) # 가중치 합 저장 리스트

for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append([v, cost])

start, end = map(int, input().split())

def dijkstra(num):
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

dijkstra(start)

print(weight[end])