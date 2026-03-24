# 16236 아기 상어

import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, size):
    visited = [[-1] * N for _ in range(N)]

    Q = deque()
    Q.append([x, y])
    visited[x][y] = 0

    fish = []
    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[cx][cy]+1
                    Q.append([nx, ny]) 

                    if 0 < graph[nx][ny] < size:
                        fish.append([visited[nx][ny], nx, ny])
    
    if not fish:
        return None
    
    fish.sort()

    return fish[0]

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

start = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 9:
            i, j = x, y
            graph[x][y] = 0

size = 2
eat = 0
time = 0

while True:
    result = bfs(i, j, size)
    
    if result is None:
        break

    dist, nx, ny = result
    time += dist

    graph[nx][ny] = 0
    eat += 1

    i, j = nx, ny

    if eat == size:
        eat = 0
        size += 1

print(time)