# 1717 집합의 표현

import sys
sys.setrecursionlimit(1000000)

def find_root(x):
    if (parent[x] == x):
        return x
    parent[x] = find_root(parent[x])

    return parent[x]

def union_parent(a, b):
    a = find_root(a)
    b = find_root(b)

    if (a < b):
        parent[b] = a

    else:
        parent[a] = b

def same_parent(a, b):
    return find_root(a) == find_root(b)

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

for _ in range(M):
    cmd, a, b = map(int, input().split())

    # 집합의 합연산
    if (cmd == 0):
        union_parent(a, b)

    elif (cmd == 1):
        if same_parent(a, b):
            print("YES")
        else:
            print("NO")