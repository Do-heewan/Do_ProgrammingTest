# 20040 사이클 게임

import sys
input = sys.stdin.readline

answer = 100_000_000

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
    return find_root(x) == find_root(y)

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

for cnt in range(1, M+1):
    a, b = map(int, input().split())

    if not same_root(a, b):
        union(a, b)

    else:
        answer = min(answer, cnt)

print(answer if answer != 100_000_000 else 0)