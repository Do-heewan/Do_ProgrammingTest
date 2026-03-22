# 13549 숨바꼭질 3

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = 0

    while Q:
        c = Q.popleft()

        if c == K: return
        
        nc = 2*c
        if 0 <= nc <= 100000 and visited[nc] == -1:
            Q.append(nc)
            visited[nc] = visited[c]

        for ix in [c-1, c+1]:
            if 0 <= ix <= 100000 and visited[ix] == -1:
                Q.append(ix)
                visited[ix] = visited[c]+1

N, K = map(int, input().split())
visited = [-1] * (100000+1)

bfs(N)

print(visited[K])