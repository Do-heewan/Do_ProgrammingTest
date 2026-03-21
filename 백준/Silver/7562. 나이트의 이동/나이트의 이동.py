# 7562 나이트의 이동

import sys
input = sys.stdin.readline

from collections import deque

move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

T = int(input())

for _ in range(T):
    L = int(input())
    curr = list(map(int, input().split()))
    target = list(map(int, input().split()))

    graph = [[-1] * L for _ in range(L)]

    Q = deque()
    Q.append((curr[0], curr[1]))
    graph[curr[0]][curr[1]] = 0

    while Q:
        cx, cy = Q.popleft()

        if [cx, cy] == target:
            print(graph[cx][cy])
            break

        for m in move:
            nx = cx + m[0]
            ny = cy + m[1]

            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == -1:
                Q.append((nx, ny))
                graph[nx][ny] = graph[cx][cy]+1