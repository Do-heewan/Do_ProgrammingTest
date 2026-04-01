# 17398 통신망 분할

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find_root(x):
    if x == parent[x]: return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    x = find_root(a)
    y = find_root(b)

    if x == y:
        return 0

    # 작은 쪽을 큰 쪽에 붙이기 (선택)
    if x > y:
        x, y = y, x

    parent[y] = x

    cost = size[x] * size[y]
    size[x] += size[y]

    return cost

def same_root(x, y):
    return find_root(x) == find_root(y)

N, M, Q = map(int, input().split())

parent = [i for i in range(N+1)]
size = [1] * (N+1)

edges = [[]]
for _ in range(M):
    a, b = map(int, input().split())
    edges.append([a, b])

query = ([int(input()) for _ in range(Q)])
removed = set(query)

# 1. 쿼리에 존재하지 않는 간선 먼저 추가
for i in range(1, M+1):
    if i not in removed:
        a = edges[i][0]
        b = edges[i][1]
        union(a, b)

# 2. 쿼리 순서 반대로 간선 추가 및 연결
query.reverse()

c = 0
for q in query:
    a = edges[q][0]
    b = edges[q][1]

    if not same_root(a, b):
        c += union(a, b)

print(c)