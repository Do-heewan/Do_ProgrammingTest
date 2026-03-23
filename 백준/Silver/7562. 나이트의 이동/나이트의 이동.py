import sys
input = sys.stdin.readline
from collections import deque

move = [(1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)]

T = int(input())

for _ in range(T):
    L = int(input())
    curr = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))

    if curr == target:
        print(0)
        continue

    graph = [[-1] * L for _ in range(L)]

    Q = deque([curr])
    graph[curr[0]][curr[1]] = 0

    while Q:
        cx, cy = Q.popleft()

        if (cx, cy) == target:
            print(graph[cx][cy])
            break

        for dx, dy in move:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == -1:
                graph[nx][ny] = graph[cx][cy] + 1
                Q.append((nx, ny))