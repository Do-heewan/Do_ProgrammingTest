# 14940 쉬운 최단거리

from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0 ,0]

N, M = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]

Q = deque()
for i in range(N):
    for j in range(M):
        if (mat[i][j] == 2) and not (visited[i][j]): # 시작점
            visited[i][j] = True
            mat[i][j] = 0

            Q.append([i, j])

            while Q:
                ci, cj = Q.popleft()

                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]

                    # 다음 노드가 1이고 방문하지 않은 경우
                    if (0 <= ni < N) and (0 <= nj < M) and (mat[ni][nj] == 1) and not (visited[ni][nj]):
                        visited[ni][nj] = True
                        mat[ni][nj] += mat[ci][cj]
                        Q.append([ni, nj])

for i in range(N):
    for j in range(M):
        if (mat[i][j] == 1) and not (visited[i][j]):
            mat[i][j] = -1

for ix in mat:
    print(*ix)