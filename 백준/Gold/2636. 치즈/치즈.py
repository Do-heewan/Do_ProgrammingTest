# 2636 치즈

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    cheeze = []
    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = True

                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    cheeze.append([nx, ny])

    return cheeze

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
cheezes = []
while True:
    visited = [[False] * M for _ in range(N)]
    res = bfs(0, 0)

    if not res:
        break
    
    for r in res:
        graph[r[0]][r[1]] = 0
    
    cnt += 1
    cheezes.append(len(res))

if cheezes:
    print(len(cheezes))
    print(cheezes[-1])
else:
    print(0)
    print(0)