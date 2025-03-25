# 2178 미로 탐색

from collections import deque

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    line = input()
    li = []

    for ix in line:
        li.append(int(ix))

    matrix.append(li)

visited = [[0 for _ in range(M)] for _ in range(N)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = 1

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0) and (matrix[nx][ny] == 1):
                visited[nx][ny] = visited[cx][cy] + 1
                Q.append([nx, ny])

    return visited[N-1][M-1]

print(bfs(0, 0))