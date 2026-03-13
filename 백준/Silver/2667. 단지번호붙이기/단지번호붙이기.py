# 2667 단지 번호붙이기

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    cnt = 1
    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == "1":
                    cnt += 1
                    Q.append([nx, ny])
                    visited[nx][ny] = True
    
    return cnt

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * N for _ in range(N)]

village = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == "1" and not visited[x][y]:
            res = bfs(x, y)
            village.append(res)

print(len(village))
for v in sorted(village):
    print(v)