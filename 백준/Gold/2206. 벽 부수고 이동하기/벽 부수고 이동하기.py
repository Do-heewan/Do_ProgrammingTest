# 2206 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j, w):
    Q = deque()
    Q.append([i, j, w])
    visited[i][j][w] = 1

    while Q:
        cx, cy, cw = Q.popleft()

        if cx == N-1 and cy == M-1:
            return visited[cx][cy][cw]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][cw] == 0:
                    visited[nx][ny][cw] = visited[cx][cy][cw] + 1
                    Q.append([nx, ny, cw])
                
                elif graph[nx][ny] == 1 and cw == 0 and visited[nx][ny][cw] == 0:
                    visited[nx][ny][1] = visited[cx][cy][cw] + 1
                    Q.append([nx, ny, 1])

    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 0))