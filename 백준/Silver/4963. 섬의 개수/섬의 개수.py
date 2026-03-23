# 4963 섬의 개수

from collections import deque

dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(x, y):
    if visited[x][y]: return 0

    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    Q.append([nx, ny])
                    visited[nx][ny] = True
    return 1

while True:
    N, M = map(int, input().split())

    if (N, M) == (0, 0):
        break

    graph = []
    for _ in range(M):
        graph.append(list(map(int, input().split())))

    visited = [[False] * N for _ in range(M)]

    rand = 0
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                rand += bfs(x, y)

    print(rand)