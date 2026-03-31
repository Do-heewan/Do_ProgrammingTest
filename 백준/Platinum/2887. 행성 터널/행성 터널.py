# 2887 행성 터널

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

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]

edges = []
for dim in range(3):
    rank = []
    for i in range(1, N+1):
        rank.append([pos[i-1][dim], i])
    sorted_pos = sorted(rank)
    for i in range(N-1):
        a_idx = sorted_pos[i][1]
        b_idx = sorted_pos[i+1][1]
        weight = abs(sorted_pos[i+1][0] - sorted_pos[i][0])

        edges.append([a_idx, b_idx, weight])

edges.sort(key=lambda x : x[2])

costs = 0
cnt = 0
for a, b, cost in edges:
    if cnt == N-1:
        break

    if not same_root(a, b):
        union(a, b)
        cnt += 1
        costs += cost

print(costs)