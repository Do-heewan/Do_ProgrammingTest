# 1012 유기농 배추

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    if visited[x][y]:
        return 0

    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    Q.append([nx, ny])
                    visited[nx][ny] = True
    
    return 1

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    visited = [[False] * M for _ in range(N)]
    
    res = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                res += bfs(x, y)

    print(res)