# 7576 토마토

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(tomatoes):
    Q = deque()

    for tx, ty in tomatoes:
        Q.append([tx, ty])
        visited[tx][ty] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    Q.append([nx, ny])
                    graph[nx][ny] = graph[cx][cy]+1

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]

tomatoes = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            tomatoes.append([x, y])

bfs(tomatoes)

res = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            print(-1)
            exit()
        res = max(res, graph[x][y])

print(res - 1)