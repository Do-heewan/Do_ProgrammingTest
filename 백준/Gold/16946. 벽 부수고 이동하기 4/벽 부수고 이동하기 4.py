# 16946 벽 부수고 이동하기 4

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, id):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = id

    cnt = 1
    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != id:
                # 벽이라면, 해당 공간을 포함한 0인 공간이 몇 개 이어져 있는지 확인
                if graph[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = id
                    cnt += 1

    return cnt

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append([int(i) for i in input()])

visited = [[-1] * M for _ in range(N)]
group = {}

id = 1
for x in range(N):
    for y  in range(M):
        if graph[x][y] == 0 and visited[x][y] == -1:
            res = bfs(x, y, id)
            group[id] = res
            id += 1

for x in range(N):
    for y in range(M):
        cnt = 0
        if graph[x][y] == 1:
            cnt += 1
            injeop = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != -1:
                    if visited[nx][ny] not in injeop:
                        injeop.append(visited[nx][ny])
            
            for ix in injeop:
                cnt += group[ix]
            print(cnt % 10, end='')

        else:
            print(cnt, end='')

    print()