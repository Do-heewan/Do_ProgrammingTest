# 10026 적록색약 (DFS)

import sys
sys.setrecursionlimit(100000)

N = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = []
for _ in range(N):
    word = input()
    graph_2 = []
    for ix in word:
        graph_2.append(ix)
    graph.append(graph_2)

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N) and (graph[x][y] == graph[nx][ny]) and not visited[nx][ny]:
            dfs(nx, ny)

# 정상인
non_blind = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            non_blind += 1

# 적록색약
for i in range(N):
    for j in range(N):
        if (graph[i][j] == "G"):
            graph[i][j] = "R"

blind = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            blind += 1

print(non_blind, blind)