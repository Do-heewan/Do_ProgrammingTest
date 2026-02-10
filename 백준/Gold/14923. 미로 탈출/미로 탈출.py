# 14923 미로 탈출

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y, 0])
    visited[x][y][0] = 0

    while Q:
        cx, cy, brake = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 내 존재하고, 방문하지 않은 공간일 때
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 공간일 경우
                if matrix[nx][ny] == 0 and visited[nx][ny][brake] == -1:
                    Q.append([nx, ny, brake])
                    visited[nx][ny][brake] = visited[cx][cy][brake] + 1
                
                # 벽이고 아직 벽을 부수지 않은 경우
                elif matrix[nx][ny] == 1 and brake == 0 and visited[nx][ny][1] == -1:
                    Q.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[cx][cy][brake] + 1

N, M = map(int, input().split())

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

bfs(start_x-1, start_y-1)

print(min(visited[end_x-1][end_y-1]))