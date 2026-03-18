# 10026 적록색약

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, color):

    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    Q.append([nx, ny])
                    visited[nx][ny] = True
        
    return 1

def isDeficiency(x, y, color):

    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if (color == "R" or color == "G") and (graph[nx][ny] == "R" or graph[nx][ny] == "G"):
                    Q.append([nx, ny])
                    visited[nx][ny] = True
                elif graph[nx][ny] == color:
                    Q.append([nx, ny])
                    visited[nx][ny] = True
        
    return 1

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * N for _ in range(N)]

normal = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            normal += bfs(x, y, graph[x][y])

visited = [[False] * N for _ in range(N)]

deficiency  = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            deficiency += isDeficiency(x, y, graph[x][y])

print(normal, deficiency)