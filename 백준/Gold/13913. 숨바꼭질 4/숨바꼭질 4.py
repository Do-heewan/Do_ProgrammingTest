# 13913 숨바꼭질 4

from collections import deque

def bfs(n, k):
    Q = deque()
    Q.append(n)
    visited[n] = 0

    while Q:
        curr = Q.popleft()

        if curr == k:
            return

        for next in [curr-1, curr+1, 2*curr]:
            if 0 <= next <= 100000 and visited[next] == -1:
                Q.append(next)
                visited[next] = visited[curr] + 1
                route[next] = curr

N, K = map(int, input().split())
visited = [-1] * (100_001)
route = [0 for _ in range(100001)]

bfs(N, K)

result = []
node = K
while node != N:
    result.append(node)
    node = route[node]
result.append(N)

print(visited[K])
print(*result[::-1])