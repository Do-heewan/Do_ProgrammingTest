# 15900 나무 탈출

import sys
sys.setrecursionlimit(10**5*6) # 정점이 50만까지 들어가기에, 호출 깊이가 50만까지 가능해야함.
input=sys.stdin.readline

def dfs(n):
    visited[n] = True

    for ix in graph[n]:
        if not visited[ix]:
            paths[ix] = paths[n] + 1
            dfs(ix)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

paths = [0] * (N+1)
dfs(1)

print('YNeos'[sum(paths[i] for i in range(2,N+1) if len(graph[i])==1)%2==0::2])