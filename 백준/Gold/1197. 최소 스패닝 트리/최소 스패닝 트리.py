# 1197 최소 스패닝 트리 (Kruskal)

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find_root(x):
    if x != parent[x]:
        parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    x = find_root(a)
    y = find_root(b)
    if x > y: parent[x] = y
    else: parent[y] = x

def same_root(x, y):
    return find_root(x) == find_root(y)

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]

graph.sort(key=lambda x : x[2])

parent = [i for i in range(V+1)]

cost = 0
for a, b, c in graph:
    if not same_root(a, b):
        union(a, b)
        cost += c

print(cost)