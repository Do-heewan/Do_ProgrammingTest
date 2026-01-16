# 1738 골목길

INF = 1_000_000_000

def bellman_ford(start):
    distance[start] = 0 # 시작 지점의 이동 거리는 0

    for i in range(N):
        for j in range(M):
            curr_node = edges[j][0] # 현재 노드
            next_node = edges[j][1] # 다음 노드
            edge_cost = edges[j][2] # 그때의 비용

            # 현재 노드가 순환 사이클에 존재하지 않고, 다음 노드로 이동하는 비용이 더 크다면,
            if distance[curr_node] != -INF and distance[next_node] < distance[curr_node] + edge_cost:
                distance[next_node] = distance[curr_node] + edge_cost
                route[next_node] = curr_node # 현재 노드로 오기 위해서 이전 노드의 정보를 저장한다.

                # 순환 사이클 발생
                if i == N-1:
                    distance[next_node] = INF

N, M = map(int, input().split())

distance = [-INF] * (N+1) # 각 노드별로 거리 저장 리스트
route = [0 for _ in range(N+1)] # 현재 노드에서 이어진 다음 노드
edges = [] # 간선 저장 리스트
for _ in range(M):
    a, b, weight = map(int, input().split())
    edges.append([a, b, weight])

bellman_ford(1) # 1번 노드부터 출발

# 경로 역추적
result = [N]
if distance[N] != INF:
    node = N

    # 1번 노드까지 도달할 때 까지
    while node != 1:
        node = route[node] # 현재 노드에서 이전 노드로 역추적
        result.append(node) # result에 저장

    result.reverse() # 역방향이기에 뒤집고
    print(*result) # 출력

# 마지막 지점에서 비용이 무한대라면 -1 출력
else:
    print(-1)