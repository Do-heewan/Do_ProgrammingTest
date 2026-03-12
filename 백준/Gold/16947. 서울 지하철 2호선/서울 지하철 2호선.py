# 16947 서울 지하철 2호선

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def dfs(node, start, cnt):
    # 현재 방문 점과 시작점이 같고, 지금까지 방문한 노드 수가 2개 이상이면
    if node == start and cnt >= 2:
        cycle[node] = True
        return

    visited[node] = True

    for ix in graph[node]:
        if not visited[ix]:
            dfs(ix, start, cnt+1)
        elif ix == start and cnt >= 2:
            dfs(ix, start, cnt)

def bfs():
    Q = deque()
    for i in range(1, N+1):
        if cycle[i]:
            Q.append(i)
            visited[i] = 0

    while Q:
        curr = Q.popleft()

        for ix in graph[curr]:
            if visited[ix] == -1:
                visited[ix] = visited[curr]+1
                Q.append(ix)

    return

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle = [False] * (N+1)

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i, 0)

visited = [-1] * (N+1)
bfs()

for i in range(1, N+1):
    print(visited[i], end=' ')