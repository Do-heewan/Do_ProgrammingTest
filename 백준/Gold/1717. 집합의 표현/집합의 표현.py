# 1717 집합의 표현

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find_root(x):
    if (parent[x] == x): return x
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

for _ in range(M):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        if not same_root(a, b):
            union(a, b)
    else:
        print("YES" if same_root(a, b) else "NO")