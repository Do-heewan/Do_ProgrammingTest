# 1261 알고스팟

from collections import deque

INF = 100_000_000

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = 0

    while Q:
        cx, cy = Q.popleft()

        if [cx, cy] == [N-1, M-1]:
            break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == "0":
                    if visited[nx][ny] > visited[cx][cy]:
                        visited[nx][ny] = visited[cx][cy]
                        Q.appendleft([nx, ny])
                
                else:
                    if visited[nx][ny] > visited[cx][cy]+1:
                        visited[nx][ny] = visited[cx][cy]+1
                        Q.append([nx, ny])

M, N = map(int, input().split())
graph = [list(input()) for _ in range(N)]

visited = [[INF] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])