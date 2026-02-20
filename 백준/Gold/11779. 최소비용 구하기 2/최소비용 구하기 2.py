# 11779 최소비용 구하기 2

import heapq

INF = 1_000_000_000

def dijkstra(node, weight):
    heap = []
    heapq.heappush(heap, (weight, node))
    distance[node] = 0

    while heap:
        wgt, curr = heapq.heappop(heap)

        if distance[curr] < wgt: # 현재의 가중치가 저장된 가중치보다 크다면
            continue

        for next, cost in graph[curr]:
            weight = wgt + cost
            if weight < distance[next]:
                distance[next] = weight
                route[next] = curr
                heapq.heappush(heap, (weight, next))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())

distance = [INF] * (N+1)
route = [0 for _ in range(N+1)] # 현재 노드에서 이어진 다음 노드

dijkstra(start, 0)

min_distance = distance[end]
print(min_distance)

# 경로 역추적
result = [end]
if distance[end] != INF:
    node = end

    # 1번 노드까지 도달할 때 까지
    while node != start:
        node = route[node] # 현재 노드에서 이전 노드로 역추적
        result.append(node) # result에 저장

result.reverse() # 역방향이기에 뒤집고
print(len(result))
print(*result) # 출력