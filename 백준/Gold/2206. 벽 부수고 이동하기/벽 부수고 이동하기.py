# 2206 벽 부수고 이동하기

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    Q = deque()
    Q.append([0, 0, 0])
    visited[0][0][0] = 1

    while Q:
        cx, cy, isBreak = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][isBreak] == -1:
                # 벽이 아니라면
                if graph[nx][ny] == "0":
                    Q.append([nx, ny, isBreak])
                    visited[nx][ny][isBreak] = visited[cx][cy][isBreak]+1

                # 벽이라면 부술지 안부술지 정하기
                elif graph[nx][ny] == "1" and isBreak == 0:
                    Q.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[cx][cy][0]+1

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]

bfs()

if visited[N-1][M-1][0] == -1 and visited[N-1][M-1][1] == -1:
    print(-1)
elif visited[N-1][M-1][0] == -1:
    print(visited[N-1][M-1][1])
elif visited[N-1][M-1][1] == -1:
    print(visited[N-1][M-1][0])
else:
    print(min(visited[N-1][M-1][0], visited[N-1][M-1][1]))