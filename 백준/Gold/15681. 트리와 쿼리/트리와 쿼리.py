# 15681 트리와 쿼리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, R, Q = map(int, input().split())

# 양방향 그래프 생성
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

visited = [False for _ in range(N+1)] # 방문 체크 표시 및 서브트리의 개수 저장

def dfs(root):
    visited[root] = 1 # 나 자신 먼저 포함

    for ix in graph[root]: # 자식 노드에 대해서
        if not (visited[ix]): # 방문하지 않았더라면
            visited[root] += dfs(ix) # 나 + 자식 노드의 서브트리 정점 개수

    return visited[root] # 정점 트리 개수 리턴

dfs(R) # 루트가 R일 때 모든 정점에 대해서 서브트리의 정점의 개수가 visited에 저장

for _ in range(Q):
    print(visited[int(input())])