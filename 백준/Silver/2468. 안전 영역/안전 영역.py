# 2468 안전영역

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, limit):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] >= limit:
                Q.append([nx, ny])
                visited[nx][ny] = True

    return 1

N = int(input())

graph = []
low_h = 101
high_h = 0
for _ in range(N):
    g = list(map(int, input().split()))
    graph.append(g)
    low_h = min(low_h, min(g))
    high_h = max(high_h, max(g))

res = 0
for i in range(low_h, high_h+1):
    visited = [[False] * N for _ in range(N)]
    area = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y] >= i:
                area += bfs(x, y, i)

    res = max(res, area)

print(res)