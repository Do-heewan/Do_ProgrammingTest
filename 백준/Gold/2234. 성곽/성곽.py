# 2234 성곽

from collections import deque

direction = [1, 2, 4, 8]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y, room_id):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = room_id
    cnt = 1

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            # 벽이 존재하는지 체크
            if matrix[x][y] & (1 << i):
                continue

            # 벽이 없는 방향으로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = room_id
                Q.append([nx, ny])
                cnt += 1

    return cnt

N, M = map(int, input().split())

matrix = []
for _ in range(M):
    matrix.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(M)]
room_size = {}
room_id = 0

# 방의 개수 및 각 방의 크기 찾기
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            room_id += 1
            room_size[room_id] = bfs(i, j, room_id)

merge_room_size = 0
# 방 아이디가 서로 다른 방끼리 맞닿은 벽을 허물었을 때 크기
for x in range(M):
    for y in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[x][y] != visited[nx][ny]:
                    a = room_size[visited[x][y]]
                    b = room_size[visited[nx][ny]]
                    merge_room_size = max(merge_room_size, a + b)

print(len(room_size))
print(max(room_size.values()))
print(merge_room_size)