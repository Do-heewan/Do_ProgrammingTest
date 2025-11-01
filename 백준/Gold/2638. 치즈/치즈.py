# 2638 치즈

from collections import deque

def air():
    Q = deque()
    Q.append([0, 0])
    visited[0][0] = 1

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    Q.append([nx, ny])
                    visited[nx][ny] = 1

                elif graph[nx][ny] == 1:
                    visited[nx][ny] += 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    visited = [[0] * M for _ in range(N)] # 방문 횟수 저장

    air()
    time += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                graph[i][j] = 0

    air_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                air_cnt += 1
    
    if air_cnt == (N * M):
        break

print(time)