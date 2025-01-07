# 11724  연결 요소의 개수

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 그래프 초기화
visited = [False] * (N+1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향

def bfs(start_v, visited):
    Q = deque([start_v])

    while Q:
        c = Q.popleft()

        for nx in graph[c]:
            if not (visited[nx]):
                visited[nx] = True
                Q.append(nx)

    return 1

for i in range(1, N+1):
    if not (visited[i]):
        count += bfs(i, visited)

print(count)