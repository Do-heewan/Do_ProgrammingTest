import sys
input = sys.stdin.readline

# 1012 유기농 배추

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    li = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        li[y][x] = 1

    visited = [[0] * M for _ in range(N)]
    bug = 0
    for x in range(N):
        for y in range(M):
            if (li[x][y] == 1) and (visited[x][y] == 0):
                Q = deque()
                Q.append((x, y))
                
                while Q:
                    cx, cy = Q.popleft()

                    for i in range(4):
                        n_x = cx + dx[i]
                        n_y = cy + dy[i]

                        if (0 <= n_x < N) and (0 <= n_y < M) and (li[n_x][n_y] == 1) and (visited[n_x][n_y] == 0):
                            visited[n_x][n_y] = 1
                            Q.append((n_x, n_y))

                bug += 1

    print(bug)