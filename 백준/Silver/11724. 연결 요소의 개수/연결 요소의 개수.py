# 11724  연결 요소의 개수 (DFS)

import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 그래프 초기화
visited = [False] * (N+1) # 방문 여부
count = 0 # 트리 탐색

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향

# 깊이 우선 탐색(재귀 함수)
def dfs(start_v, visited):
    visited[start_v] = True

    for nx in graph[start_v]:
        if not (visited[nx]):
            dfs(nx, visited)

    return 1

for i in range(1, N+1):
    if not (visited[i]):
        count += dfs(i, visited)

print(count)