# 13549 숨바꼭질 3

from collections import deque

N, K = map(int, input().split()) # N = 현재 위치, K = 찾아가야 할 위치

MAX = 100_000
visited = [0 for _ in range(MAX+1)]

def bfs(start, end):
    Q = deque()
    Q.append(start)

    while Q:
        c = Q.popleft()

        if (c == end):
            return visited[c]
        
        for ix in [2*c, c-1, c+1]:
            if (0 <= ix <= MAX) and (visited[ix] == 0):
                if (ix == 2*c):
                    visited[ix] = visited[c]

                else:
                    visited[ix] = visited[c] + 1

                Q.append(ix)

print(bfs(N, K))