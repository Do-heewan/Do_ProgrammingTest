# 2667 단지번호붙이기

from collections import deque

N = int(input())

# 지도 생성
map = [[] for _ in range(N)]
for i in range(N):
    num = input()
    for ix in num:
        map[i].append(int(ix))

# 방문여부 체크
visited = [[False] * N for _ in range(N)]

# action(상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

house = 0
apart = []
for x in range(N):
    for y in range(N):
        if (map[x][y] == 1) and not (visited[x][y]):
            visited[x][y] = True
            house += 1
            
            Q = deque()
            Q.append([x, y])

            while Q:
                cx, cy = Q.popleft()

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if (0 <= nx < N) and (0 <= ny < N) and (map[nx][ny] == 1) and not (visited[nx][ny]):
                        visited[nx][ny] = True
                        Q.append((nx, ny))
                        house += 1

        if (house != 0):
            apart.append(house)
            house = 0

apart.sort()

print(len(apart))
for ix in apart:
    print(ix)