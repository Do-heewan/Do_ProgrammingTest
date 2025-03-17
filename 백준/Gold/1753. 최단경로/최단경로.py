# 1753 최단 경로

import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split()) # V개의 정점, E개의 간선

start = int(input()) # 시작 정점

INF = 1_000_000_000 # 아주 큰 값 설정
graph = [[] for _ in range(V+1)] 
weight = [INF] * (V+1) # 가중치 합 저장 리스트

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w)) # 시작 정점에 (끝 정점, 가중치) 저장

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

for i in range(1, len(weight)):
    if (weight[i] == INF): # 가중치가 바뀌지 않은 경우, 도달 할 수 없음
        print("INF")

    else:
        print(weight[i])