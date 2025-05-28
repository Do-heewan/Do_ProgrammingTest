# 10026 적록색약

from collections import deque

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

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny] == graph[x][y]) and not visited[nx][ny]:
                Q.append([nx, ny])
                visited[nx][ny] = True

# 정상인
non_blind = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
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
            bfs(i, j)
            blind += 1

print(non_blind, blind)