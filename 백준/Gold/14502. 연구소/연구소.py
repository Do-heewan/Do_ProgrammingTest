# 14502 연구소

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    visited = [[False] * M for _ in range(N)]
    Q = deque()
    
    for x, y in virus:
        Q.append([x, y])
        visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = True

    cnt = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0 and not visited[x][y]:
                cnt += 1

    return cnt

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

walls = []
virus = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            walls.append([x, y])
        elif graph[x][y] == 2:
            virus.append([x, y])

L = len(walls)
ans = 0

for i in range(L-2):
    for j in range(i+1, L-1):
        for k in range(j+1, L):
            graph[walls[i][0]][walls[i][1]] = 1
            graph[walls[j][0]][walls[j][1]] = 1
            graph[walls[k][0]][walls[k][1]] = 1

            ans = max(ans, bfs())

            graph[walls[i][0]][walls[i][1]] = 0
            graph[walls[j][0]][walls[j][1]] = 0
            graph[walls[k][0]][walls[k][1]] = 0

print(ans)