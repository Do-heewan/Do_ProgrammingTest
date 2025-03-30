# 1197 최소 스패닝 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

V, E = map(int, input().split())

tree = []
for _ in range(E):
    a, b, c = map(int, input().split())
    tree.append((a, b, c))
tree.sort(key = lambda x : x[2]) # c(cost)에 대해서 오름차순 정렬

parent = [i for i in range(V+1)]

def get_parent(x):
    if (parent[x] == x):
        return x

    parent[x] = get_parent(parent[x])

    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if (a < b):
        parent[b] = a

    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in tree:
    if not (same_parent(a, b)):
        union_parent(a, b)
        answer += cost

print(answer)