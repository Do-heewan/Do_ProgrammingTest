# 1167 트리의 지름

import sys
sys.setrecursionlimit(10**6)

def dfs(node, dist):
    global max_distance, far_node
    visited[node] = True

    if max_distance < dist:
        max_distance = dist
        far_node = node

    for ix, c in graph[node]:
        if not visited[ix]:
            visited[ix] = True
            dfs(ix, dist+c)
            visited[ix] = False

V = int(input())

graph = [[] for _ in range(V+1)]
for i in range(1, V+1):
    ipt = list(map(int, input().split()))
    start = ipt[0]
    for i in range(1, len(ipt[:-1]), 2):
        graph[start].append((ipt[i], ipt[i+1]))

visited = [False] * (V+1)
max_distance = 0
far_node = 0

dfs(1, 0)

visited = [False] * (V+1)
dfs(far_node, 0)

print(max_distance)