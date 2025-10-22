from collections import deque

# 방향: 상, 좌, 우, 하 (문제 조건상 우선순위: 상->좌)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(sx, sy, size):
    visited = [[-1] * N for _ in range(N)]
    visited[sx][sy] = 0
    q = deque([(sx, sy)])
    fish = []  # 먹을 수 있는 물고기 후보

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 이동 가능 조건
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # 먹을 수 있는 물고기라면 후보에 추가
                    if 0 < graph[nx][ny] < size:
                        fish.append((visited[nx][ny], nx, ny))

    # 먹을 물고기가 없다면 None 반환
    if not fish:
        return None
    # 거리, 행, 열 순으로 정렬
    fish.sort()
    dist, fx, fy = fish[0]
    return fx, fy, dist


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 초기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0  # 빈칸 처리
            break

size = 2
eat = 0
time = 0

while True:
    result = bfs(shark_x, shark_y, size)
    if result is None:
        break
    x, y, dist = result

    time += dist
    eat += 1
    graph[x][y] = 0
    shark_x, shark_y = x, y

    # 크기 증가 조건
    if eat == size:
        size += 1
        eat = 0

print(time)