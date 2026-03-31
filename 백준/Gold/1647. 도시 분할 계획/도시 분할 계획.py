# 1647 도시 분할 계획

import sys
input = sys.stdin.readline

def find_root(x):
    if x == parent[x]: return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    x = find_root(a)
    y = find_root(b)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def same_root(x, y):
    return  find_root(x) == find_root(y)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

edges.sort(key=lambda x : x[2])

parent = [i for i in range(N+1)]

costs = 0
max_cost = 0
for a, b, cost in edges:
    if not same_root(a, b):
        union(a, b)
        costs += cost
        max_cost = max(max_cost, cost)

print(costs - max_cost)