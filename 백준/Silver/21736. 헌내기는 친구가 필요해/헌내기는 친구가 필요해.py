# 21736 헌내기는 친구가 필요해

from collections import deque

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = []
for _ in range(N):
    word = input()
    words = []
    for ix in word:
        words.append(ix)
    graph.append(words)

visited = [[False] * M for _ in range(N)]
person = 0

for i in range(N):
    for j in range(M):
        if (graph[i][j] == "I"):
            sx, sy = i, j

Q = deque()
Q.append([sx, sy])

while Q:
    x, y = Q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
            if (graph[nx][ny] == "O"):
                Q.append([nx, ny])
                visited[nx][ny] = True
            elif (graph[nx][ny] == "P"):
                Q.append([nx, ny])
                visited[nx][ny] = True
                person += 1
            else:
                visited[nx][ny] = True

print(person if person != 0 else "TT")