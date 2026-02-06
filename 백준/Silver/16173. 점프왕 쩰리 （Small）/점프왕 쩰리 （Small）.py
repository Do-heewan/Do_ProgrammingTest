# 16173 점프왕 쩰리

from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()
        jump = game[cx][cy]

        for nx, ny in [[cx, cy+jump], [cx+jump, cy]]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                Q.append([nx, ny])
                visited[nx][ny] = True

N = int(input())

game = []
for _ in range(N):
    game.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

bfs(0, 0)

print("HaruHaru" if visited[-1][-1] else "Hing")