# 16988 Baaaaaaaaaduk2 (Easy)

from collections import deque
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

def bfs(x, y, visited):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    cnt = 1
    isPossible = True

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if baduk[nx][ny] == 0:
                isPossible = False

            elif 0 <= nx < N+2 and 0 <= ny < M+2 and not visited[nx][ny] and baduk[nx][ny] == 2:
                Q.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1

    if not isPossible:
        return 0
    else:
        return cnt

baduk = []
baduk.append([1] * (M+2))
for _ in range(N):
    baduk.append([1] + list(map(int, input().split())) + [1])
baduk.append([1] * (M+2))

blank = []
for i in range(N+2):
    for j in range(M+2):
        if baduk[i][j] == 0:
            blank.append([i, j])
blanks = list(combinations(blank, 2))

max_score = 0
for one, two in blanks:
    x1 = one[0]
    x2 = two[0]
    y1 = one[1]
    y2 = two[1]

    baduk[x1][y1] = 1
    baduk[x2][y2] = 1
    visited = [[False] * (M+2) for _ in range(N+2)]

    score = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if baduk[i][j] == 2 and not visited[i][j]:
                score += bfs(i, j, visited)

    max_score = max(max_score, score)

    baduk[x1][y1] = 0
    baduk[x2][y2] = 0

print(max_score)