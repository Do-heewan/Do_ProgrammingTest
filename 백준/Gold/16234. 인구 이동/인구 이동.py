# 16234 인구 이동

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    union = [[x, y]]
    total = graph[x][y]

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(graph[cx][cy] - graph[nx][ny])

                if L <= diff <= R:
                    visited[nx][ny] = True
                    Q.append([nx, ny])
                    union.append([nx, ny])
                    total += graph[nx][ny]
    
    return union, total

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

days = 0
while True:
    visited = [[False] * (N) for _ in range(N)]
    moved = False

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                union, total = bfs(x, y)

                if len(union) > 1:
                    moved = True
                    avg = total // len(union)

                    for i, j in union:
                        graph[i][j] = avg

    if not moved:
        break

    days += 1

print(days)