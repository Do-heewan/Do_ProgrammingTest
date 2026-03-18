# 7569 토마토

import sys
input = sys.stdin.readline

from collections import deque

def bfs(tomatoes):
    Q = deque()
    
    for x, y, h in tomatoes:
        Q.append([x, y, h])

    while Q:
        cx, cy, ch = Q.popleft()

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nh = ch + dh[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and graph[nh][ny][nx] == 0:
                if graph[nh][ny][nx] == 0:
                    graph[nh][ny][nx] = graph[ch][cy][cx] + 1
                    Q.append([nx, ny, nh])

N, M, H = map(int, input().split())

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]

graph = []
for _ in range(H):
    g = []
    for _ in range(M):
        g.append(list(map(int, input().split())))
    graph.append(g)

tomatoes = []
for h in range(H):
    for y in range(M):
        for x in range(N):
            if graph[h][y][x] == 1:
                tomatoes.append([x, y, h])

bfs(tomatoes)

ans = 0
for h in range(H):
    for y in range(M):
        for x in range(N):
            if graph[h][y][x] == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, graph[h][y][x])

print(ans-1)