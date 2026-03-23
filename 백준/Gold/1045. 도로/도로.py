# 1045 도로

def root_find(x):
    if x == parent[x]: return parent[x]
    parent[x] = root_find(parent[x])
    return parent[x]

def union(a, b):
    x = root_find(a)
    y = root_find(b)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def same_root(x, y):
    return root_find(x) == root_find(y)

N, M = map(int, input().split())

edges = []
for i in range(N):
    lst = list(input())
    for j in range(i, N):
        if lst[j] == "Y":
            edges.append([i, j])

edges.sort()

parent = [i for i in range(N)]

road = []
for edge in edges:
    x = edge[0]
    y = edge[1]

    if not same_root(x, y):
        union(x ,y)
        road.append([x, y])

if len(road) != N-1:
    print(-1)
    exit()

for edge in edges:
    if edge not in road:
        road.append(edge)

    if len(road) == M:
        break

if len(road) < M:
    print(-1)
    exit()

indegree = [0] * N
for r in road:
    a = r[0]
    b = r[1]
    indegree[a] += 1
    indegree[b] += 1

print(*indegree)