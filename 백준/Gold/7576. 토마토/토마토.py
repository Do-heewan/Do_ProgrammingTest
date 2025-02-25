# 7576 토마토

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

# action (Up, Down, Left, Right)
dx = [0, 0, -1, 1]
dy = [1 ,-1 ,0 ,0]

Q = deque() # 큐 생성
visited = [[False] * M for _ in range(N)] # 방문 표시

# 익은 토마토의 위치 찾기
for i in range(N):
    for j in range(M):
        if (mat[i][j] == 1) and not (visited[i][j]):
            visited[i][j] = True
            Q.append((i, j))

# 익은 토마토들에 대해서
while Q:
    cx, cy = Q.popleft()

    # 상, 하, 좌, 우 이동
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        # 익지 않은 토마토라면
        if (0 <= nx < N) and (0 <= ny < M) and (mat[nx][ny] == 0) and not (visited[nx][ny]):
            # 날짜 수를 계산하기 위해 현재 토마토의 일수 + 1
            mat[nx][ny] = mat[cx][cy] + 1
            Q.append((nx, ny)) # 익은 토마토 추가

# matrix 전체를 돌며
for i in range(N):
    for j in range(M):
        # 익지 않은  토마토를 발견한 경우, 이는 모두를 익게 할 수 없다는 뜻
        if (mat[i][j] == 0):
            print(-1)
            exit(0) # -1 출력 후 종료

# mat내부에 가장 큰 수 => 모든 토마토가 익는데 걸린 시간 => 9일째 -> 8일 걸림 / 만약 max값이 1이라면 0 출력
print((max(max(row) for row in mat) - 1) if max(mat) != 1 else 0)