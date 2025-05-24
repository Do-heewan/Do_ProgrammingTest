# 7569 토마토

import sys
from collections import deque
# input = sys.stdin.readline

N, M, H = map(int, input().split())

# 상, 하, 좌, 우, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

graph = []
for _ in range(H):
    graph_2 = []
    for _ in range(M):
        graph_2.append(list(map(int, input().split())))
    graph.append(graph_2)

visited = [[[False for _ in range(N)] for _ in range(M)] for _ in range(H)]
Q = deque()

# 토마토 위치 찾기
for h in range(H):
    for y in range(M):
        for x in range(N):
            if (graph[h][y][x] == 1):
                Q.append([h, y, x])
                visited[h][y][x] = 1

while Q:
    ch, cy, cx = Q.popleft()

    for i in range(6):
        nh = ch + dh[i]
        ny = cy + dy[i]
        nx = cx + dx[i]

        if (0 <= nh < H) and (0 <= ny < M) and (0 <= nx < N) and (graph[nh][ny][nx] == 0) and not visited[nh][ny][nx]:
            Q.append([nh, ny, nx])
            visited[nh][ny][nx] = visited[ch][cy][cx] + 1

for h in range(H):
    for y in range(M):
        for x in range(N):
            if not visited[h][y][x] and graph[h][y][x] == 0:
                print(-1)
                exit(0)

max_value = 0
for h in range(H):
    for y in range(M):
        for x in range(N):
            max_value = max(max_value, visited[h][y][x])

print(max_value - 1 if max_value != 1 else 0)