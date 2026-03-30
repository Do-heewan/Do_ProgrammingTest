# 1261 알고스팟

import heapq

INF = 100_000_000

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra(x, y):
    weight[x][y] = 0

    heap = []
    heapq.heappush(heap, [0, x, y])

    while heap:
        wgt, cx, cy = heapq.heappop(heap)

        if wgt > weight[cx][cy]:
            continue
            
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                cost = wgt + int(graph[nx][ny])
                if weight[nx][ny] > cost:
                    weight[nx][ny] = cost
                    heapq.heappush(heap, [cost, nx, ny])

M, N = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

weight = [[INF] * M for _ in range(N)]

dijkstra(0, 0)

print(weight[N-1][M-1])