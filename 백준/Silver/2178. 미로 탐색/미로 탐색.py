# 2178 미로 탐색

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = 1

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if graph[nx][ny] == "1":
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[cx][cy]+1

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[-1] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])