# 16928 뱀과 사다리 게임

from collections import deque

N, M = map(int, input().split())

graph = []
visited = [False for _ in range(106)] # 주사위 횟수 저장

for _ in range(N+M):
    a, b = map(int, input().split())
    graph.append([a, b])

def bfs(num):
    pos = num

    Q = deque()
    Q.append(pos)

    visited[pos] = 0

    while Q:
        c = Q.popleft()

        if (c == 100):
            return visited[c]

        for i in range(1, 7):
            nc = c + i

            for a, b in graph:
                if (a == nc):
                    nc = b

            if not visited[nc]:
                visited[nc] = visited[c] + 1
                Q.append(nc)

print(bfs(1))