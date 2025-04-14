# 1865 웜홀

T = int(input())

INF = 1_000_000_000

def bellman_ford(start):
    distance[start] = 0
    # 전체 노드 반복
    for i in range(N):
        # 매 반복마다 모든 간선 확인
        for j in range(len(edge)):
            curr_node = edge[j][0]
            next_node = edge[j][1]
            edge_cost = edge[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
            if (distance[next_node] > distance[curr_node] + edge_cost):
                distance[next_node] = distance[curr_node] + edge_cost

                # v번째에서 값이 갱신된다면 음수 순환이 존재
                if (i == N - 1):
                    return True
                
    return False

for _ in range(T):
    N, M, W = map(int, input().split())

    edge = []
    distance = [INF for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        edge.append([S, E, T])
        edge.append([E, S, T])

    # 웜홀 정보 (T가 음수)
    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append([S, E, -T])

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")