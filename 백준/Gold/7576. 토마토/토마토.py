# 7576 토마토

from collections import deque

M, N = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

# action (Up, Down, Left, Right)
dx = [0, 0, -1, 1]
dy = [1 ,-1 ,0 ,0]

visited = [[False] * M for _ in range(N)]

Q = deque()

count = 0
for i in range(N):
    for j in range(M):
        if (mat[i][j] == 1) and not (visited[i][j]):
            visited[i][j] = True
            Q.append((i, j))

while Q:
    cx, cy = Q.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and (mat[nx][ny] == 0) and not (visited[nx][ny]):
            mat[nx][ny] = mat[cx][cy] + 1
            Q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if (mat[i][j] == 0):
            print(-1)
            exit(0)

print((max(max(row) for row in mat) - 1) if max(mat) != 1 else 0)