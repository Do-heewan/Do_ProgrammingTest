# 20040 사이클 게임

import sys
input = sys.stdin.readline

def find_root(x):
    if (parent[x] == x): return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union_set(a, b):
    x = find_root(a)
    y = find_root(b)
    if (x > y):
        parent[x] = y 
    else: 
        parent[y] = x

def same_root(a, b):
    return find_root(a) == find_root(b)

N, M = map(int, input().split())

parent = [i for i in range(N)]
res = 0
for i in range(1, M+1):
    a, b = map(int, input().split())

    if same_root(a, b):
        print(i)
        exit()
    union_set(a, b)

else:
    print(0)