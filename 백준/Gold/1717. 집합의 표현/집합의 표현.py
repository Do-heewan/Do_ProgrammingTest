# 1717 집합의 표현

import sys
sys.setrecursionlimit(1000000)

def find_root(x):
    if (parent[x] == x): return x
    parent[x] = find_root(parent[x])
    return parent[x]

def same_root(a, b):
    return find_root(a) == find_root(b)

def union_set(a, b):
    x = find_root(a)
    y = find_root(b)
    if (x > y):
        parent[x] = y 
    else: 
        parent[y] = x

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
for _ in range(M):
    cmd, a, b = map(int, input().split())

    if (cmd == 0):
        union_set(a, b)

    elif (cmd == 1):
        print("YES") if same_root(a, b) else print("NO")