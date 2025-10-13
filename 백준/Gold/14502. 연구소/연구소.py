# 14502 연구소

import sys
import copy
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    Q = deque()

    test_map = copy.deepcopy(graph)
    for x in range(N):
        for y in range(M):
            if test_map[x][y] == 2:
                Q.append([x, y])

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and test_map[nx][ny] == 0:
                test_map[nx][ny] = 2
                Q.append([nx, ny])

    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                cnt += 1

    result = max(result, cnt)

def create_wall(count):
    if count == 3:
        bfs()
        return
    
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                graph[x][y] = 1
                create_wall(count+1)
                graph[x][y] = 0


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

create_wall(0)

print(result)