# 13913 숨바꼭질 4

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = 0

    while Q:
        c = Q.popleft()

        if c == K: break

        for next_ in [c-1, c+1, 2*c]:
            if 0 <= next_ <= 100_000 and visited[next_] == -1:
                visited[next_] = visited[c]+1
                route[next_] = c
                Q.append(next_)

N, K = map(int, input().split())

visited = [-1] * 100001
route = [-1] * 100001

bfs(N)

print(visited[K])

result = []
curr = K
while curr != -1:
    result.append(curr)
    curr = route[curr]

result.reverse()
print(*result)