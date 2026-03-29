# 1520 내리막 길

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[x][y] > graph[nx][ny]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

print(dfs(0, 0))